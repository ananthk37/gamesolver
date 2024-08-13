from flask import Flask
from flask_cors import CORS
server = Flask(__name__)
CORS(server)

from .app import solvers

if __name__ == "__main__":
    server.run(debug=True)