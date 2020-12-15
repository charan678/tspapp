from random import randint
import requests, time

SERVER_URL="http://localhost:5000/"

def publish_path(vehical_id):
    visited_locations = []
    for i in range(0, 10):
        visited_locations.append({ "latitude": randint(0, 300), "longitude": randint(0, 300)})
    request_body = {"id": vehical_id, "locations" : visited_locations}
    resp = requests.post(SERVER_URL + f"/vehical/visit/", json=request_body)
    if resp.status_code == 200:
        print("path visited published")

def find_shortest_path(vehical_id):
    for retry in range(0,5):
        time.sleep(10)
        resp = requests.get(SERVER_URL + f"/vehical/path/{vehical_id}")
        if resp.status_code == 200:
            print(f"shortest path = {resp.content}")
            break

if __name__ == '__main__':
    publish_path(101)
    find_shortest_path(101)