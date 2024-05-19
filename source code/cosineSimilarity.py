import scipy
import pickle
with open("./tfidfValues", "rb") as f:
    di = pickle.load(f)

def findCosineSimilarity(q,alldocs): #pass len of all docs
    sim = dict()
    z = list(di.values())
    for i in range(len(alldocs)):
        c = 1 - scipy.spatial.distance.cosine(q, z[i])
        sim[i] = c
    # simOfTopTen = sorted(sim.items(), key=lambda x: x[1])[:-11:-1]
    return sim
