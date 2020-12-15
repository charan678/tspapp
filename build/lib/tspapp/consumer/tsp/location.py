from __future__ import annotations
import math

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

    def compute_euclidean_distance(self, to_location):
        return (int(
            math.hypot((self.latitude - to_location.latitude),
                       (self.longitude - to_location.longitude))))
