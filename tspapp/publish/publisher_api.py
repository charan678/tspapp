import os
from flask import Flask
from flask_restful import Resource, Api, reqparse
import uuid
import logging

from tspapp.publish.store import VehicalStore
from tspapp.queue.queue_connection import RabbitMq

app = Flask(__name__)
api = Api(app)


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s:%(message)s')
logger = logging.getLogger(__name__)

AMPQ_URL= os.environ.get("AMQP_URL", "localhost")
QUEUE_NAME=os.environ.get("QUEUE_NAME", "localhost")
rabbit_mqueue = RabbitMq(AMPQ_URL, QUEUE_NAME)
store = VehicalStore()
parser = reqparse.RequestParser()

class ShortestPath(Resource):
    def get(self, path_id):
        return {"pathId": path_id, "shortestPath":[]}

class Vehical(Resource):
    def post(self):
        args = parser.parse_args()
        logging.debug(args)
        # path =  uuid.uuid1()
        # data["pathId"] = path
        # store.add(data)
        # rabbit_mqueue.publish_message(data)
        return {"pathId": 1}

api.add_resource(Vehical, '/vehical/visit/')
api.add_resource(ShortestPath, '/path/<string:path_id>')

if __name__ == '__main__':
    app.run(debug=True,  host='0.0.0.0')