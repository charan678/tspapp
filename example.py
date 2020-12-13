from random import randint
import requests, time

SERVER_URL="http://localhost:5000/"

def publish_path(path, vehical_id):
    while True:
        visited_locations = []
        for i in range(0, 10):
            visited_locations.append({"latitude": randint(0, 300), "longitude": randint(0, 300)})
        request_body = {"id" : vehical_id, "locations" : visited_locations}
        resp = requests.post(SERVER_URL + f"/vehical/visit/{vehical_id}", data = request_body)
        if resp.status_code == 200:
            print("path visited published")

def find_shortest_path(path_id):
    for retry in range(0,5):
        time.sleep(10)
        resp = requests.get(SERVER_URL + f"/path/{path_id}")
        if resp.status_code == 200:
            print(f"shortest path = {resp}")
            break

if __name__ == '__main__':
    path_id = publish_path()
    find_shortest_path(path_id)