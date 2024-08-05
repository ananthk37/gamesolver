from ..server import server
from flask import jsonify

@server.route('/health', methods=['GET'])
def head():
    return jsonify("Hello!")