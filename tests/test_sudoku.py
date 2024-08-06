import pytest
import json

with open("tests/test_data/sudoku_test.json", "r") as f:
    data = json.load(f)
    testdata = [(x["input"],x["solution"]) for x in data["boards"]]

@pytest.mark.parametrize("problem,solution", testdata)
def test_sudoku_solver(problem, solution, client):
    response = client.post("/sudoku",json={
        "board": problem
    })
    assert response.json["board"] == solution