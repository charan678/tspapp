import os
from flask import Flask
from flask_restful import Resource, Api, reqparse, request
import uuid
import json
from tspapp import logger

from tspapp.publish.store import VehicalStore
from tspapp.queue.queue_connection import RabbitMq

app = Flask(__name__)
api = Api(app)

AMPQ_URL = os.environ.get("AMQP_URL", "localhost")
QUEUE_NAME = os.environ.get("QUEUE_NAME", "localhost")
rabbit_mqueue = RabbitMq(AMPQ_URL, QUEUE_NAME)
store = VehicalStore()
parser = reqparse.RequestParser()


class ShortestPath(Resource):
    def get(self, path_id):
        return {"pathId": path_id, "shortestPath": []}


class Vehical(Resource):
    def post(self):
        logger.debug("post request ")
        data = request.json
        requestId = str(uuid.uuid1())
        data["requestId"] = requestId
        store.add(data)
        rabbit_mqueue.connect()
        rabbit_mqueue.publish_message(json.dumps(data))
        return {"requestId": requestId}


api.add_resource(Vehical, '/vehical/visit/')
api.add_resource(ShortestPath, '/path/<string:path_id>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
