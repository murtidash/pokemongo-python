from datetime import datetime
import time
import json


class Pokemon():
    _meta = None
    
    def boo(self):
        return "boo"

    def __init__(self, meta):
        self._meta = meta

    def get_location(self):
        return {'latitude': self._meta['latitude'], 'longitude': self._meta['longitude']}
    
    def get_id(self):
        return self._meta['pokemon_id']
    
    def get_name(self):
        return self._meta['pokemon_name']
    
    def get_expires_timestamp(self):
        return self._meta['expires']
    
    def get_expires(self):
        return datetime.fromtimestamp(self.get_expires_timestamp())

    def get_json(self):
        location = self.get_location()
        data = {'pokemon':str(self.get_name()),'id':str(self.get_id()),'lat':str(location['latitude']),'long':str(location['longitude']),'expires':str(int(self.get_expires_timestamp() - time.time())),'time':str(time.strftime("%H:%M",time.localtime()))}
        #data = [ ('pokemon',self.get_name()),('id',self.get_id()),('lat',location['latitude']),('long',location['longitude']),('time',self.get_expires_timestamp() - time.time()) ]
        return data
        #return json.dumps(data,sort_keys=True,  indent=4, ensure_ascii=True)

    def __repr__(self):
        location = self.get_location()
        
        return '%s [%d]: %f, %f, %d seconds left' % (
                                                     self.get_name(),
                                                     self.get_id(),
                                                     location['latitude'],
                                                     location['longitude'],
                                                     int(self.get_expires_timestamp() - time.time())
                                                     )

    def __str__(self):
        location = self.get_location()
        return '%s [%d]: %f, %f, %d seconds left' % (
                                                     self.get_name(),
                                                     self.get_id(),
                                                     location['latitude'],
                                                     location['longitude'],
                                                     int(self.get_expires_timestamp() - time.time())
                                                     )