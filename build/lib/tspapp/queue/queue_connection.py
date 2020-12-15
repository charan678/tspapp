import pika
from tspapp import logger


class RabbitMq:
    def __init__(self, url, queue, exchange=''):
        self.url = url
        self.queue = queue
        self.connection = None
        self.exchange = exchange
        self.channel = None

    def connect(self):
        params = pika.URLParameters(self.url)
        params.socket_timeout = 5
        self.connection = pika.BlockingConnection(params)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue)

    def publish_message(self, message):
        logger.debug(message)
        self.channel.basic_publish(
            exchange=self.exchange,
            routing_key=self.queue,
            body=message)

    def consumer_callback(self, callback_function, start_consuming=True):
        self.channel.basic_consume(
            queue=self.queue,
            on_message_callback=callback_function,
            auto_ack=True)
        if start_consuming:
            self.channel.start_consuming()

    def close(self):
        self.connection.close()

    def __enter__(self):
        self.connection()

    def __exit__(self):
        self.close()
