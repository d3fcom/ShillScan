import os
import logging
from flask import Flask

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# create the app
app = Flask(__name__)

# No database needed - we'll use in-memory storage
logger.info("Running in local mode with mock data")

# Import models here (now just mock data classes)
from models import Token

# Import routes
from routes import *

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)