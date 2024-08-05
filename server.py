from flask import Flask

server = Flask(__name__)

import app.solvers


server.run(debug=True)