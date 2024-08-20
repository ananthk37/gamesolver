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

@pytest.mark.parametrize("board,groups,size,solution", testdata)
def test_kenken_solver(board, groups, size, solution, client):
    response = client.post("/kenken", json={
        "board": board,
        "groups": groups,
        "size": size
    })
    assert response.json["board"] == solution