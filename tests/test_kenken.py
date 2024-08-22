import pytest
import json

with open("tests/test_data/kenken_test.json", "r") as f:
    data = json.load(f)
    testdata = [(
            x["input_board"],
            x["input_groups"],
            x["board_size"],
            x["solution"] )
        for x in data["boards"]
    ]
    badtests = [(
        x["input_board"],
        x["input_groups"],
        x["board_size"]) 
        for x in data["unsolveable"]
    ]

@pytest.mark.parametrize("board,groups,size,solution", testdata)
def test_kenken_solver(board, groups, size, solution, client):
    response = client.post("/kenken", json={
        "board": board,
        "groups": groups,
        "size": size
    })
    assert response.json["board"] == solution

@pytest.mark.parametrize("board,groups,size", badtests)
def test_unsolveable_kenken(board, groups, size, client):
    response = client.post("/kenken", json={
        "board": board,
        "groups": groups,
        "size": size
    })
    assert response.status_code == 400