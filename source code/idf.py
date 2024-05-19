import math

def inverseDocumentFrequency(term,alldocs):
    numOfDocsWithGivenTerm = 0
    for i in range(len(alldocs)):
        if term.lower() in alldocs[i].lower().split():
            numOfDocsWithGivenTerm += 1
        
    if numOfDocsWithGivenTerm > 0:
        return math.log(len(alldocs)/numOfDocsWithGivenTerm)
    else:
        return 0