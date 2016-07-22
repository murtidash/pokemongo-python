from utils.pokemon import Pokemon
import json
import copy

class Spawns():
    _json_data = None
    jsonf = open('poke.json','a+')
    

    def __init__(self, filename):    
        self._jsonData = open(filename).read()
        #filename.close()
    
    def remove_duplicates(self):
        data=json.loads(self._jsonData)
        data2=copy.deepcopy(data)
        toremove=[]

        for i in xrange(len(data["spawns"])):
            #print str(i)+" checking"+json.dumps(data["spawns"][i])
            for j in xrange(len(data["spawns"])):
                if i not in toremove:
                    #print(str(j)+" not in " + str(toremove))
                    if data["spawns"][i]["id"] == data["spawns"][j]["id"]:
                        if data["spawns"][i]["long"] == data["spawns"][j]["long"]:
                            if (data["spawns"][i]["lat"] == data["spawns"][j]["lat"]) and (data["spawns"][i]["time"] != data["spawns"][j]["time"]):
                                #print("adding "+str(j)+" to toremove")
                                toremove.append(j)
                else:
                    #print (str(j)+" in "+str(toremove))
                    break
            #print "toremove: "+str(toremove)
        toremove.sort(reverse=True)
        for k in xrange(len(toremove)):
            print ("deleting "+str(data2["spawns"][toremove[k]]))
            del data2["spawns"][toremove[k]]
        return data2

    def save(self,filename):
        jsonf2=open(filename,'w')
        json.dump(self._jsonData, jsonf2, indent=4, ensure_ascii=False)
        print(json.dumps(self._jsonData, indent=4))
        jsonf2.close()
