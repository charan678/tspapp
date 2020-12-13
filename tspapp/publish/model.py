
class Location:
    def __init__(self, latitude, longitude):
        self._latitude = latitude
        self._longitude = longitude
    @property
    def latitude(self):  
        return self._latitude

    @property
    def longitude(self):  
        return self._longitude
    
    @latitude.setter
    def latitude(self, value):
        self._latitude = value

    @longitude.setter
    def longitude(self, value):
        self._longitude = value


class Vehical:
    
    def __init__(self, vehical_id, locations=[]):
        self._vehical_id = vehical_id
        self._locations: [Location] = locations
        self._shortest_path = None

    @property
    def vehical_id(self):  
        return self._vehical_id

    @property
    def locations(self):
        return self._locations
    
    @property
    def shortest_path(self):
        return self._shortest_path
    
    @vehical_id.setter
    def vehical_id(self, value):
        self._vehical_id = value

    @shortest_path.setter
    def shortest_path(self, value):
        self._shortest_path = value
    
    @locations.setter
    def locations(self, value):
        self._locations= value

    def __dict__(self):
        return {
            "vehical_id": self._vehical_id,
            "locations": [location.__dict__() for location in self._locations],
        }