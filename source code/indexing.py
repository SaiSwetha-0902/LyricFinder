import os
from nltk.corpus import stopwords

def invertedIndex(index,alldocs,os,pattern,stop_words):
    for file in os.listdir():
        id = file.split(".")[0]
        f = open(file,'r',encoding='utf8')
        # gives the each word in that document
        words = pattern.finditer(f.read())
        tx = []
        for word in words:
            s = word.group().lower()
            tx.append(s)
            if s in stop_words:
                continue
            if s not in index.keys():
                index[s] = [[id,1]]
            else:
                if index[s][-1][0] !=id:
                    index[s].append([id,1])
                else:
                    index[s][-1][1] += 1;
        f.close()
        cont = " ".join(tx);
        # all the documents are added to the list called alldocs
        alldocs[int(id)] = cont
