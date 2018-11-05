from flask import Flask, jsonify, request
import numpy as np

app = Flask(__name__)


@app.route("/name", methods=["GET"])
def name():
    name = {
            "name": "Katelyn"
            }
    return jsonify(name)


@app.route("/hello/<name>", methods=["GET"])
def hello(name):
    message = {
            "message": "Hello there, " + name
            }
    return jsonify(message)


@app.route("/distance", methods=["POST"])
def distance():
    req_data = request.get_json()
    a = req_data["a"]
    b = req_data["b"]
    dist = calcDistance(a, b)

    data = {
            "distance": dist,
            "a": a,
            "b": b
            }

    return jsonify(data)


def calcDistance(a, b):
    delta_x = a[0] - b[0]
    delta_y = a[1] - b[1]
    dist = np.sqrt(np.square(delta_x) + np.square(delta_y))
    return dist

if __name__ == "__main__":
    app.run(host="127.0.0.1")
