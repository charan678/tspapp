import os
import json

from tspapp.queue.queue_connection import RabbitMq
from tspapp import logger
from tspapp.consumer.tsp.vehical import Vehical
from tspapp.consumer.tsp.first_solution_strategy import FirstSolutionStrategy
import requests

PUBLISHER_URL = os.environ.get('PUBLISHER_SERVER')

def callback(ch, method, properties, body):
    logger.info(" [x] Received %r" % body)
    data = json.loads(body)
    vehical = Vehical(data['id'])
    vehical.add_locations(data['locations'])
    tspalgo = FirstSolutionStrategy(vehical)
    shortest_path = tspalgo.find_shortest_path()
    requests.patch(f"{PUBLISHER_URL}/vehical/visit/101", json={"shortest_path": shortest_path})
    logger.info(".... consumed message ....")

if __name__ == "__main__":
    AMPQ_URL = os.environ.get("AMQP_URL", "localhost")
    QUEUE_NAME = os.environ.get("QUEUE_NAME", "localhost")
    rabbit_mqueue = RabbitMq(AMPQ_URL, QUEUE_NAME)
    rabbit_mqueue.connect()
    rabbit_mqueue.consumer_callback(callback)
