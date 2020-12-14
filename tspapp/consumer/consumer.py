import os
import json

from tspapp.queue.queue_connection import RabbitMq
from tspapp import logger
from tspapp.consumer.tsp.vehical import Vehical
from tspapp.consumer.tsp.first_solution_strategy import FirstSolutionStrategy

def callback(ch, method, properties, body):
    logger.info(" [x] Received %r" % body)
    data = json.load(body)
    vehical = Vehical(data['id'])
    vehical.add_location(data['locations'])
    tspalgo = FirstSolutionStrategy()
    logger.info("shortest path is = ", tspalgo.find_shortest_path())




if __name__ == "__main__":
    AMPQ_URL = os.environ.get("AMQP_URL", "localhost")
    QUEUE_NAME = os.environ.get("QUEUE_NAME", "localhost")
    rabbit_mqueue = RabbitMq(AMPQ_URL, QUEUE_NAME)
    rabbit_mqueue.connect()
    rabbit_mqueue.consumer_callback(callback)
