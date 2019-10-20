import modeltrain as mt
import json
with open('user_map.txt') as json_file:
    user_map = json.load(json_file)

def getsamplepeople():
    tojsonkey = []
    mtinp = mt.findgoodinps()
    for i in list(mtinp)[:6]:
        tojsonkey.append(user_map[i])


    tojsonvalue = []
    for i in list(mtinp)[:6]:
        tojsonvalue.append(mt.makemodel(i)[1])

    tojson = {list(mtinp)[i] : [tojsonkey[i],tojsonvalue[i]] for i in range(len(tojsonkey))}


    with open('idtonameandattr.txt', 'w') as outfile:
        json.dump(tojson,outfile)

getsamplepeople()





