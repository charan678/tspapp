import os
from flask import Flask
from flask_restful import Resource, Api, reqparse, request
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


@app.route('/vehical/path/<string:vehical_id>', methods=['GET'])
def vehical_path(vehical_id):
    logger.debug(f"vehical path requested {vehical_id}")
    return json.dumps(store.get(vehical_id))

@app.route("/vehical/visit/", methods=['POST'])
def vehical_visits():
    logger.debug("post request ")
    data = request.json
    store.add(data)
    rabbit_mqueue.connect()
    rabbit_mqueue.publish_message(json.dumps(data))
    return json.dumps({"id": data["id"]})

@app.route("/vehical/visit/<string:vehical_id>", methods=['PATCH'])
def vehical_update_shortest_path(vehical_id):
    shortest_path = request.json['shortest_path']
    logger.info(f"shortest path is = {shortest_path} for vehical = {vehical_id}")
    output = store.update(vehical_id, 'shortest_path', shortest_path)
    logger.debug(f"output = {output}")
    return json.dumps(output)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
