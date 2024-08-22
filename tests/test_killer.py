import pytest
import json

with open("tests/test_data/killer_test.json", "r") as f:
    data = json.load(f)
    testdata = [(x["input_board"], x["input_groups"], x["solution"]) for x in data["boards"]]
    badtests = [(x["input_board"], x["input_groups"]) for x in data["unsolveable"]]

@pytest.mark.parametrize("board,groups,solution", testdata)
def test_killer_solver(board, groups, solution, client):
    print(board)
    print(groups)
    response = client.post("/killer",json={
        "board": board,
        "groups": groups
    })
    assert response.json["board"] == solution


@pytest.mark.parametrize("board,groups", badtests)
def test_unsolveable_kenken(board, groups, client):
    response = client.post("/killer", json={
        "board": board,
        "groups": groups,
    })
    assert response.status_code == 400