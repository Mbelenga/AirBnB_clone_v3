#!/usr/bin/python3
"""A script for creating a Flask application"""

import os
from flask import Flask
from models import storage
from api.v1.views import app_views
from flask_cors import CORS

# An instance of  a Flask application
app = Flask(__name__)

# Register the blue print app_views
app.register_blueprint(app_views)

# Initializing cors
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

# Declare a method to handle teardown
@app.teardown_appcontext
def teardown(exception):
    storage.close()

@app.errorhandler(404)
def page_not_found(error):
    return ({'error': 'Not found'}), 404

if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
