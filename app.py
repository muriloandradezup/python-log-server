#!/usr/bin/python

import datetime
import logging
import sys
import json_logging
import flask

app = flask.Flask(__name__)
json_logging.ENABLE_JSON_LOGGING = True
json_logging.init(framework_name='flask')
json_logging.init_request_instrument(app)

# init the logger as usual
logger = logging.getLogger("test-logger")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))


@app.route('/start/<int:id>')
def start(id):
    logger.info('started_purchase', extra={'props': {'transaction_id': id}})
    return 'Started transaction %s' % id


@app.route('/finish/<int:id>')
def finish(id):
    logger.info('finished_purchase', extra={'props': {'transaction_id': id}})
    return 'Finished transaction %s' % id


@app.route('/')
def home():
    return "UP "


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(8080), use_reloader=False)
