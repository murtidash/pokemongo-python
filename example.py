import copy
import time
import json
from  utils.spawns import Spawns
from skiplagged import Skiplagged
from config import *


if __name__ == '__main__':
    client = Skiplagged()
    
    bounds = (
                #Hollyberry
                #(34.053, -84.365), (34.061,-84.345)
                #Roswell
                (34.002572,-84.3799717), (34.074266,-84.3040977)
              )

    
    spawnpoints=Spawns('poke.json')
    print(json.dumps(spawnpoints._jsonData))
    spawnpoints.remove_duplicates()
    spawnpoints.save('poke2.json')

    while 0:
        try:
            # Log in with a Google or Pokemon Trainer Club account
            print client.login_with_google(userName. password)
            # print client.login_with_pokemon_trainer('USERNAME', 'PASSWORD')
            
            # Get specific Pokemon Go API endpoint
            print client.get_specific_api_endpoint()
            
            # Get profile
            print client.get_profile()
            
            # Find pokemon
            for pokemon in client.find_pokemon(bounds):
                print pokemon
                txtf.write(str(pokemon)+"\n")
                jsonf.write(json.dumps(pokemon.get_json())+"\n")
                txtf.flush()
                jsonf.flush()
        except Exception as e:
            print "exception:", e
            time.sleep(1)
        except KeyboardInterrupt:
            break
    print("saving file")
    