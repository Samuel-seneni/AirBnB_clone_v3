#!/usr/bin/python3
"""Defines flask aplications"""

from models import storage
from os import getenv
<<<<<<< HEAD
from flask import Flask
=======
>>>>>>> 09654c9b27b567a78269cfe9e39ee9cca1a149e2
from api.v1.views import app_views
from flask import Flask, jsonify, abort
from flask_cors import CORS

app = Flask(__name__)

app.register_blueprint(app_views)


if __name__ == '__main__':
    HOST = getenv('HBNB_API_HOST', '0.0.0.0')
    PORT = int(getenv('HBNB_API_PORT', 5000))
    app.run(host=HOST, port=PORT, threaded=True)
