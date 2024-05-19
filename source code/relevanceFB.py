import pickle
import numpy as np

with open("tfidfValues","rb") as f:
    di = pickle.load(f)

def findNewQueryRocchio(q,lst,feedback):
    docNonRel = []
    docRel = []
    for i in range(len(lst)):
        if feedback[i] == 1:
            docRel.append(lst[i][0])
        else:
            docNonRel.append(lst[i][0])
        

    uDR = np.zeros(len(di[0]))
    for i in range(len(docRel)):
        uDR = uDR+di[docRel[i]]

    uDNR = np.zeros(len(di[0]))
    for i in range(len(docNonRel)):
        uDNR = uDNR+di[docNonRel[i]]
    
    Qnew = q + 0.75*(uDR/len(docRel)) + 0.25*(uDNR/len(docNonRel))
    return Qnew


# relevance feedback
# feedbackList  = dict()
# feedbackList[query] = [1,1,0,0,1,1,1,0,0,0]


# with open("./feedbackList", "rb") as f:
#     feedbackList = pickle.load(f)

# feedbackTakenUser = [0, 1, 1, 1, 0, 0, 1, 0, 0, 0]
# new_list = list(map(add, feedbackList[query], feedbackTakenUser))
# feedbackList[query] = new_list
# outFile = open("feedbackList", "wb")
# pickle.dump(feedbackList, outFile)
# outFile.close()

# with open("./feedbackList", "rb") as f:
#     feedbackList = dict(pickle.load(f))

# if query in feedbackList.keys():
#     print("re ranked the documents by already given relevance feedback:")
#     new_lst = [0]*10
#     for i in range(len(feedbackList[query])):
#         new_lst[i] = -feedbackList[query][i]
#     new_lst.sort()
#     for i in range(len(new_lst)):
#         for j in range(len(new_lst)):
#             if new_lst[i] == -feedbackList[query][j]:
#                 if j+1 in new_lst:
#                     continue
#                 else:
#                     new_lst[i] = j+1
# reOrderedDoc = []
# for i in range(len(new_lst)):
#     reOrderedDoc.append(simOfTopTen[new_lst[i]-1])
# print(reOrderedDoc)



