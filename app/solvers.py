from __main__ import server

@server.route('/health', methods=['GET'])
def head():
    return "Hello!"