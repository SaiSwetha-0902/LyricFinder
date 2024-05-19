import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import os
import re
from termFrequency import *
from idf import *
from findTfIdfValues import *
from cosineSimilarity import*
from relevanceFB import*
from PR import*
import pickle
from operator import add
import numpy
nltk.download('stopwords')

# 1
# read the csv file using pandas library
# df = pd.read_csv('./tcc_ceds_music.csv');
# # print(csvFile);

# x = df.columns

# ly = list(df[x[5]])[:28372]

# for i in range(len(ly)):
#     d = "./docs/"+str(i)+".txt"
#     f = open(d,"w",encoding="utf8");
#     f.write(ly[i]);
#     f.close();


# 2 inverted index
cwd = os.getcwd()
os.chdir(cwd+"/docs")

stop_words = set(stopwords.words('english'))
stemmer = SnowballStemmer(language='english')
index = dict()
alldocs = dict()

pattern = re.compile(r'''(?x)      
	        ([A-Z]\.)+             
        |   \$?\d+(\.\d+)?%?        
        |   \w+                   
 ''', re.VERBOSE | re.I)
i = 0


# creating inverted index
print("creating inverted index.....")
for file in os.listdir():
    id = file.split(".")[0]
    f = open(file, 'r', encoding='utf8')
    # gives the each word in that document
    words = pattern.finditer(f.read())
    tx = []
    for word in words:
        s = word.group().lower()
        tx.append(s)
        if s in stop_words:
            continue
        if s not in index.keys():
            index[s] = [[id, 1]]
        else:
            if index[s][-1][0] != id:
                index[s].append([id, 1])
            else:
                index[s][-1][1] += 1
    f.close()
    cont = " ".join(tx)
    # all the documents are added to the list called alldocs
    alldocs[int(id)] = cont

print("inverted index is created.")
os.chdir(cwd)
# store the all unique words in a list (vocabulary)
vocab = list(index.keys())
# print(len(vacab))


# add find idfValues and add values to idfValues pkl file
# idfValues = dict()

# print(len(vacab))
# print(vacab[0])

# for i in range(len(vacab)):
# finding the idf values
#     val = inverseDocumentFrequency(vacab[i], alldocs)
#     idfValues[vocab[i]] = val
#     print(i);

# outFile = open("idfValues", 'wb')
# pickle.dump(idfValues, outFile)
# outFile.close()

# inFile = open("idfValues", 'rb')
# newDict = pickle.load(inFile)
# inFile.close()

# print(newDict)


# finding the tfidfValues
with open("./idfValues", "rb") as f:
    d = pickle.load(f)
# finding tf*idf
# tfidfValues = findTfIdfValues(vocab, alldocs,d)
# outFile = open("tfidfValues","wb")
# pickle.dump(tfidfValues,outFile)
# outFile.close()

# inFile = open("idfValues","rb")
# dictnary = pickle.load(inFile)
# inFile.close()
# print(dictnary)


# ranking
print("=======================================================================================")
print("finding ranking for a given query....")
# query = "Hold Time feel break"
query = input("enter the query: ")
if (query == ""):
    print("query can't be null")
elif(query != ""):
    s = re.findall("[a-zA-Z]+", query.lower())
    uniq = set(s)
    vec = np.zeros(len(vocab))
    for j in uniq:
        if j in vocab and j in d:
            # print(j)
            tfidf = termFrequency(j, query) * d[j]
            ind = vocab.index(j)
            vec[ind] = tfidf
    q = vec
# finding cosine similair
    sim = findCosineSimilarity(q, alldocs)
    simOfTopTen = sorted(sim.items(), key=lambda x: x[1])[:-11:-1]
    print("top 10 documents are : ")
    # print(simOfTopTen)
    for i in range(len(simOfTopTen)):
        print("ID :",simOfTopTen[i][0],"similarity :",simOfTopTen[i][1],"doc :",alldocs[simOfTopTen[i][0]])
        print("---------------------------------------------------------------------------------")
    # print(simOfTopTen)


feedback = []
print("=======================================================================================")
print("enter feedback in binary of length 10 --- R -> 1 , NR -> 0 :")
for i in range(len(simOfTopTen)):
    e = int(input())
    feedback.append(e)
    
print("=======================================================================================")   
# finding Precison and Recall
PR(feedback)

print("=======================================================================================")
# new documents after taking feedback
# feedback = [1,1,1,1,1,1,1,1,1,0]
Qnew = findNewQueryRocchio(q,simOfTopTen,feedback)
sim1 = findCosineSimilarity(Qnew,alldocs)
print("top 10 documents after taking feedback : ")
simOfTopTenRFB = sorted(sim1.items(), key=lambda x: x[1])[:-11:-1]
for i in range(len(simOfTopTenRFB)):
    print("ID :", simOfTopTenRFB[i][0], "similarity :",simOfTopTenRFB[i][1], "doc :", alldocs[simOfTopTenRFB[i][0]])
    print("----------------------------------------------------------------------------------")
# print(simOfTopTenRFB)



# search based on specific filter

df = pd.read_csv("./tcc_ceds_music.csv")

# print(df['genre'].value_counts())

gen =list(df['genre'])[:28372]
filterBasedOnGenre = dict();
print("=======================================================================================")
diffGenre = {1: "pop", 2: "country", 3: "blues",
                     4: "rock", 5: "jazz", 6: "reggae", 7: "hip hop"}
print(diffGenre)
enteredGenre = input("enter a number form above based on what genre you want: ")
genreFilter = diffGenre[int(enteredGenre)]

for i in range(len(gen)):
    if gen[i] == genreFilter:
        filterBasedOnGenre[i] = sim1[i]

filterBasedOnGenre = sorted(filterBasedOnGenre.items(), key=lambda x: x[1])[:-10:-1]
for i in range(len(filterBasedOnGenre)):
    print("----------------------------------------------------------------------------------")
    print("ID :",filterBasedOnGenre[i][0],"doc :",alldocs[filterBasedOnGenre[i][0]])

# print(filterBasedOnGenre)


# search based on artist_name

artist_names = list(df['artist_name'])[:28372]
# print(artist_names)

filterBasedOnArtist_name=dict()
print("=======================================================================================")
enteredArtist_name = input("enter the artist name to search: ")

for i in range(len(artist_names)):
    if artist_names[i] == enteredArtist_name:
        filterBasedOnArtist_name[i] = sim1[i]

if (len(filterBasedOnArtist_name) > 5):
    filteredArtist_name = sorted(filterBasedOnArtist_name.items(), key=lambda x: x[1])[:-6:-1]
    for i in range(5):
        print("ID :",filteredArtist_name[i][0],"doc :",alldocs[filteredArtist_name[i][0]])
        print("----------------------------------------------------------------------------------")
    # print(filteredArtist_name)
elif(len(filterBasedOnArtist_name) == 0):
    print("No Results Found !...")
else:
    print(filterBasedOnArtist_name)
    print("----------------------------------------------------------------------------------")



