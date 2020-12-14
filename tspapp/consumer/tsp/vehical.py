import math
from tspapp.consumer.tsp.location import Location

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
        self._locations = value

    def add_location(self, latitude, longitude):
        self.locations.append(Location(latitude, longitude))

    def add_locations(self, list_lat_long):
        for val in list_lat_long:
            self.locations.append(Location(val['latitude'], val['longitude']))

    def eular_distance_locations(self):
        distances = {}
        for from_counter, from_node in enumerate(self.locations):
            distances[from_counter] = {}
            for to_counter, to_node in enumerate(self.locations):
                if from_counter == to_counter:
                    distances[from_counter][to_counter] = 0
                else:
                    distances[from_counter][to_counter] = from_node.compute_euclidean_distance(to_node)
        return distances

    def __dict__(self):
        return {
            "vehical_id": self._vehical_id,
            "locations": [location.__dict__() for location in self._locations],
        }
