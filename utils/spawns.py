from utils.pokemon import Pokemon
import json
import copy

class Spawns():
    _data = None
    _jsonData = None
    _jsonData2 = None
    jsonf = open('poke.json','a+')
    

    def __init__(self, filename):    
        self._data = open(filename).read()
        self._jsonData=json.loads(self._data)
        self._jsonData2=copy.deepcopy(self._jsonData)
        #filename.close()
    
    def remove_duplicates(self):
        
        toremove=[]
        for i in xrange(len(self._jsonData["spawns"])):
            #print str(i)+" checking"+json.dumps(data["spawns"][i])
            for j in xrange(len(self._jsonData["spawns"])):
                if i not in toremove:
                    #print(str(j)+" not in " + str(toremove))
                    if self._jsonData["spawns"][i]["id"] == self._jsonData["spawns"][j]["id"]:
                        if self._jsonData["spawns"][i]["long"] == self._jsonData["spawns"][j]["long"]:
                            if (self._jsonData["spawns"][i]["lat"] == self._jsonData["spawns"][j]["lat"]) and (self._jsonData["spawns"][i]["time"] != self._jsonData["spawns"][j]["time"]):
                                #print("adding "+str(j)+" to toremove")
                                toremove.append(j)
                else:
                    #print (str(j)+" in "+str(toremove))
                    break
            #print "toremove: "+str(toremove)
        toremove.sort(reverse=True)
        for k in xrange(len(toremove)):
            print ("deleting "+str(self._jsonData2["spawns"][toremove[k]]))
            del self._jsonData2["spawns"][toremove[k]]
        self._jsonData = self._jsonData2;

    def additem(self,pokemon):
        self._jsonData["spawns"].append(pokemon.get_json())


    def save(self,filename):
        jsonf2=open(filename,'w')
        json.dump(self._jsonData, jsonf2, sort_keys=True, indent=4, ensure_ascii=True)
        #print(json.dumps(self._jsonData,sort_keys=True,  indent=4, ensure_ascii=True))
        jsonf2.close()
