import pytest
from tspapp.consumer.tsp.vehical import Vehical
from tspapp.consumer.tsp.location import Location

def test_eular_distance_locations():
    #assign
    locations = [Location(5, 5), Location(3, 5)]
    vehical = Vehical(101, locations)

    #act
    distance = vehical.eular_distance_locations()

    #assert
    assert distance == {0: {0: 0, 1: 2}, 1: {0: 2, 1: 0}}
