from flask import Flask
server = Flask(__name__)

from .app import solvers

if __name__ == "__main__":
    server.run(debug=True)