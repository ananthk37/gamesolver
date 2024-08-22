import pytest
import json

with open("tests/test_data/sudoku_test.json", "r") as f:
    data = json.load(f)
    testdata = [(x["input"],x["solution"]) for x in data["boards"]]
    badtests = [(x["input"]) for x in data["unsolveable"]]

@pytest.mark.parametrize("problem,solution", testdata)
def test_sudoku_solver(problem, solution, client):
    response = client.post("/sudoku",json={
        "board": problem
    })
    assert response.json["board"] == solution


    
@pytest.mark.parametrize("board", badtests)
def test_unsolveable_kenken(board, client):
    response = client.post("/sudoku", json={
        "board": board,
    })
    assert response.status_code == 400