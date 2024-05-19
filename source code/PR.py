import matplotlib.pyplot as plt
P = []
R = []
def PR(lst):
    t = 0
    r = 0
    avgP = 0
    tR = lst.count(1)
    for i in lst:
        t += 1
        if(i >= 1):
            r += 1
            P.append(round(r/t,3))
            R.append(round(r/tR,3))
            avgP = avgP + r/t
        if( i == 0):
            P.append(round(r/t,3))
            R.append( round(r/tR,3))
    avgP = round(avgP*(1/r),3)
    print("Precison :",P) 
    print("Recall :",R)
    print("Average Precison :",avgP)
    plt.plot(R, P)
    plt.xlabel("RECALL")
    plt.ylabel("PRECISION")
    plt.title('PRECISION-RECALL CURVE')
    plt.show()

                   
