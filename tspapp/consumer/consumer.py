import os
from tspapp.queue.queue_connection import RabbitMq
from tspapp import logger
import json


def callback(ch, method, properties, body):
    logger.info(" [x] Received %r" % body)
    data = json.load(body)


if __name__ == "__main__":
    AMPQ_URL = os.environ.get("AMQP_URL", "localhost")
    QUEUE_NAME = os.environ.get("QUEUE_NAME", "localhost")
    rabbit_mqueue = RabbitMq(AMPQ_URL, QUEUE_NAME)
    rabbit_mqueue.connect()
    rabbit_mqueue.consumer_callback(callback)
