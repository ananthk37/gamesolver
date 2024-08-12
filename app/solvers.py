from ..server import server
from flask import jsonify, request
from ..sudoku import sudoku_solver as sudo_solver
from ..killer import killer_solver
@server.route('/health', methods=['GET'])
def head():
    return jsonify("Hello!")

@server.route("/sudoku", methods=["POST"])
def sudoku():
    board = request.json["board"]
    board_dict = sudo_solver.to_dict(board)
    solved_board = sudo_solver.solve(board_dict)
    response = {"board": solved_board}
    return jsonify(response)

@server.route("/killer", methods=["POST"])
def killer():
    board = request.json["board"]
    board_dict = sudo_solver.to_dict(board)
    board_groups = request.json["groups"]
    solved_board = killer_solver.solve(board_dict, board_groups)
    response = {"board": solved_board}
    return jsonify(response)