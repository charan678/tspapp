import pytest
from tspapp.consumer.tsp.location import Location

def test_eular_distance():
    location = Location(5, 5)

    output = location.compute_euclidean_distance(Location(1,1))

    assert output == 5
