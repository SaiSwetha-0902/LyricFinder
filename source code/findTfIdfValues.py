from termFrequency import*
import numpy as np

tfidfValues = dict()
def findTfIdfValues(vocab, alldocs, d):
    for i in range(len(alldocs)):
        s = alldocs[i].lower().split()
        uniq = set(s)
        # print(len(vocab))
        # print(i)
        vec = np.zeros(len(vocab))
        for j in uniq:
            if j in vocab and j in d:
                tfidf = termFrequency(j, alldocs[i]) * d[j]
                ind=vocab.index(j)
                vec[ind]=tfidf
                
        print(i)
        tfidfValues[i] = vec
        
    return tfidfValues

