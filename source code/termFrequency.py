import re
import math

def termFrequency(term,doc):
    split_d =re.findall("[a-zA-Z]+",doc.lower())
    term = term.lower()
    tf = 0
    for i in split_d:
        if term == i:
            tf = tf+1
    if tf > 0:
        logTf = 1+math.log(tf)
        return logTf
    else:
        return 0
            
