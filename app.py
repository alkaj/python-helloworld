import logging
from flask import Flask
from flask import json
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/status")
def status():
    app.logger.info("Status endpoint was reached")
    return app.response_class(
        response=json.dumps({"user": "admin", "result": "OK - healthy"}),
        status=200,
        mimetype='application/json'
    )


@app.route("/metrics")
def metrics():
    app.logger.info("Metrics endpoint was reached")
    return app.response_class(
        response=json.dumps(
            {"user": "admin", "data": {"UserCount": 140, "UserCountActive": 23}}),
        status=200,
        mimetype='application/json'
    )


if __name__ == "__main__":
    logging.basicConfig(filename='app.log', level=logging.DEBUG)
    app.run(host='0.0.0.0')
