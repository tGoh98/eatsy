#!/usr/bin/env python
# coding: utf-8

# In[31]:


# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 00:52:40 2019

@author: lifel
"""
import json
import numpy as np
import modeltrain as mt


# In[32]:


# In[34]:


# bovec = {}
# rejecb = []
# for i in list(bo.keys()):
#     try:
#         bovec[i] = botovec(i)
#     except:
#         rejecb.append(i)
# with open('bovec.txt', 'w') as outfile:
#     json.dump(bovec,outfile)


# In[35]:


with open('bovec.txt') as json_file:
    bovec = json.load(json_file)
# with open('buisnessoutput.txt') as json_file:
#     bo = json.load(json_file)
with open('allca.txt') as json_file:
    allca = json.load(json_file)
with open('business_map.txt') as json_file:
    business_map = json.load(json_file)


# In[36]:


def botovec(bsn):
    savesum = bo[bsn] #uncomment bo inport
    newsum = {}
#         print('got here 1')
    if not len(savesum) == 0:
#             print('got here 2')
        sumset = set(sorted(savesum.keys()))
#             catset = set([x for x in list(sumset) if x[:10] == 'categories'])
#             resset = sumset - catset
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
        return temp
    else:
        raise NameError('no data for buisness')
        


# In[64]:


busidict = np.asarray(list(bovec.values()))


# In[212]:


def make_pretty(attr):
    pretty_string = ""
    for i in range(len(attr)):
        char = attr[i]

        if char == '_':
            pretty_string += ' '
            continue

        if char.isupper() and not attr[i - 1].isupper() and not attr[i + 1].isupper() and i != 0:
            pretty_string += ' '

        pretty_string += char

    return pretty_string


# In[282]:


def buildprefs(c):
    tojson = {}
    arr = np.asarray([round(i,2) for i in c])
    arr = (arr-min(arr))/(max(arr)-min(arr))
    marr = (arr+1)*100000
#     print(marr)
#     print(max(marr),min(marr))
    top_idx = np.argsort(c)[-10:]
    top_values = [c[i] for i in top_idx]
    for idx in top_idx:
        tojson[idx] =int(round( marr[idx],0))
    
    #print(np.array([np.array(xi) for xi in list(tojson.values())]))
   
    arr2 = np.asarray(list(tojson.values()))
#     print(type(arr2),arr2)
    arr2 = (arr2-min(arr2))/(max(arr2)-min(arr2)) * 10
#     print(arr2)
    arr2 = [int(round( i,0)) for i in arr2]
    r = 3
    #list(sorted(allca))[]
    oldkey = lambda i: list(sorted(allca))[int(list(tojson.keys())[i])]
    return {make_pretty(oldkey(i)):arr2[9 - i] for i in range(r)},[int(list(tojson.keys())[i]) for i in range(r)]


# In[283]:


def meanModel(users, business):
    tojson = {}
    x = np.array(users)
    xmean = np.mean(x, axis=0)
    
    grabprefs = buildprefs(xmean)
    
    with open('grouppreferences.txt', 'w') as outfile:
        json.dump(grabprefs[0],outfile)
    
    print(grabprefs[1])
    
    xmeanT = np.transpose(xmean)
    xScored = np.dot(business, xmeanT)
    xScored = (xScored-min(xScored))/(max(xScored)-min(xScored))
    nxScored = (xScored+1)*100
    xTop5 = np.argsort(xScored)[-6:]
    
    buss = {}
    for busid in xTop5:
        prefs = {}
        for grouppref in grabprefs[1]:
            prefs[make_pretty(list(sorted(allca))[grouppref])] = bovec[list(bovec.keys())[int(busid)]][grouppref]
        
    
        
        buss[make_pretty(business_map[list(bovec.keys())[int(busid)]])] = prefs 
        
    with open('busselections.txt', 'w') as outfile:
        json.dump(buss,outfile)
    return buss


# In[284]:


with open('selectedUsers.json') as json_file:
    selus = json.load(json_file)

add = []
for i in range(len(list(selus.keys()))):
    _c = mt.makemodel(list(selus.keys())[i])[0]
    add.append(_c)
    
    
a1 = meanModel(add,busidict)


# In[ ]:





# In[ ]:





# In[ ]:




