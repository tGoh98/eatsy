# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 00:52:40 2019

@author: lifel
"""
import json
import numpy as np
import modeltrain as mt

x = mt.findgoodinps()

add = []
for i in range(10):
    _c = mt.makemodel(x[i])
    add.append(_c)
    
    
#%%

with open('buisnessoutput.txt') as json_file:
    bo = json.load(json_file)


business = np.array([list(v) for v in bo.values()])

business = business.astype(float)

#%%


def meanModel(users, business):
    x = np.array(users)
    xmean = np.mean(x, axis=0)
    xmeanT = np.transpose(xmean)
    xScored = np.matmul(business, xmeanT)
    xTop5 = np.argsort(xScored)[-5:]
    return xTop5.tolist()

def medianModel(users, business):
    x = np.array(users)
    xmean = np.median(x, axis=0)
    xmeanT = np.transpose(xmean)
    xScored = np.matmul(business, xmeanT)
    xTop5 = np.argsort(xScored)[-5:]
    return xTop5.tolist()

def avgMeanMedian(users, business):
    x = np.array(users)
    xmean = (np.median(x, axis=0) + np.mean(x, axis=0))/2
    xmeanT = np.transpose(xmean)
    xScored = np.matmul(business, xmeanT)
    xTop5 = np.argsort(xScored)[-5:]
    return xTop5.tolist()

a1 = meanModel(add,business)
a2 = medianModel(add,business)
a3 = avgMeanMedian(add,business)


print(a1)
print(a2)
print(a3)











