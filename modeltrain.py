#!/usr/bin/env python
# coding: utf-8

# In[190]:


import json
import ast
import pandas as pd
from collections import defaultdict
import time
import numpy as np
import scipy.stats
from sklearn.linear_model import LinearRegression
from sklearn.linear_model.logistic import LogisticRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model.logistic import _logistic_regression_path
import matplotlib.pyplot as plt


# In[550]:


with open('buisnessoutput.txt') as json_file:
    bo = json.load(json_file)
with open('users.txt') as json_file:
    users = json.load(json_file)


# In[551]:


with open('allattrs.txt') as json_file:
    allattrs = json.load(json_file)
with open('allcats.txt') as json_file:
    allcats = json.load(json_file)
allca = allcats + allattrs
len(allca)
with open('allca.txt', 'w') as outfile:
    json.dump(list(sorted(allca)),outfile)


# In[552]:


def vecsperuser(usr):
    vecs={}
#     print(usr)
    j = 0
    inp2 = list(users[usr].keys())
#     print(inp2)
    for bsn in inp2:
#         print ('              ',end = '\r')
#         print (round(100*i / len(inp),2),round((100*j / len(inp2)),2),end='\r')
        print (round(100*j / len(inp2),2),end='\r')
#         print(bsn)
        savesum = bo[bsn]
        newsum = {}
#         print('got here 1')
        if not len(savesum) == 0:
#             print('got here 2')
            sumset = set(sorted(savesum.keys()))
            catset = set([x for x in list(sumset) if x[:10] == 'categories'])
            resset = sumset - catset
#             print(len(savesum),'savesum',savesum)
#             print(len(catset),'catset',catset)
#             print(len(resset),'resset',resset)
            #diff = set(allattrs) - resset
            diff = set(allca) - sumset
    
#             print(len(diff),'diff')
            for differing in diff:
                newsum[differing] = False
            for res in sumset:
                newsum[res] = savesum[res]
    #         sortedkeys = sorted(list(savesum.keys()))
            if len(newsum) != 831:
                print(bsn)
                print(len(newsum),'res')
                print(sorted(list(newsum.keys())),'\n')
                print(savesum.keys(),'\n')
#             print('\n')
#             print(np.asarray(sorted(newsum.items()))[:,1])
            temp = [1 if x == "True" else 0 for x in np.asarray(sorted(newsum.items()))[:,1]]
#             print(temp)
            vecs[bsn] = temp
#         print('got here 3')
        j += 1
    return vecs


# In[561]:


def findgoodinps_helper(inp):
    vinp = vecsperuser(inp)
    vecs = np.asarray(list(vinp.values()))
    label = []
    for bsn in vinp.keys():
        users[inp]
        label.append(users[inp][bsn])

    if len(label) > 10 and not min(label) == max(label):
#         print('\r')
        return inp
#     c = LogisticRegression(random_state=0, solver='lbfgs').fit(vecs, label).coef_


# In[566]:


def findgoodinps(limit = 100):
    goodinp = []
    for inp in list(users.keys())[0:limit]:
        goodinp.append(findgoodinps_helper(inp))
    goodinp = [x for x in goodinp if not x == None]
    return goodinp


# In[531]:


def makemodel(inp):
    tojson = {}
    vinp = vecsperuser(inp)
    vecs = np.asarray(list(vinp.values()))
    label = []
    for bsn in vinp.keys():
        users[inp]
        label.append(users[inp][bsn])
    c = LogisticRegression(random_state=0, solver='lbfgs').fit(vecs, label).coef_[0]
    arr = np.asarray([round(i,2) for i in c])
    arr = (arr-min(arr))/(max(arr)-min(arr))
    marr = (arr+1)*100000
#     print(marr)
#     print(max(marr),min(marr))
    top_idx = np.argsort(c)[-10:]
    top_values = [c[i] for i in top_idx]
    for idx in top_idx:
        tojson[list(sorted(allca))[idx]] =int(round( marr[idx],0))
    arr2 = np.asarray(list(tojson.values()))
    arr2 = (arr2-min(arr2))/(max(arr2)-min(arr2)) * 10
    print(arr2)
    arr2 = [int(round( i,0)) for i in arr2]
    return c, {list(tojson.keys())[i]:arr2[9 - i] for i in range(3)}


# In[532]:


# c = makemodel(goodinp[2])

