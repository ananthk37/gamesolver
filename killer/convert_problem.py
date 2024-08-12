#converter for killer files found in https://github.com/UvA-KR16/KilerSudoku
import sys
# import re
import json

def read_input(path):
    groups = []
    solution = {}
    with open(path, "rt") as f:
        lines = f.readlines()
        for line in lines:
            group_sum, rest = line.split("=")
            # rest = rest[:-2]

            group = []
            #this is such a dumb hack
            for i in range(1, len(rest), 9):
                row, col, sol = map(int, (rest[i], rest[i+3], rest[i+6]))
                group.append(row * 9 + col)
                solution[row * 9 + col] = sol

            groups.append([int(group_sum),group])
    solution_str = ""
    for i in range(81):
        solution_str += str(solution[i])
    
    game_state = {"input_board": "0" * 81,
                  "input_groups": groups,
                  "solution": solution_str}
    return game_state
    pass

def new_file(path):
    path_list = path.split(".")
    assert(len(path_list) == 2)
    path_list[1] = "json"
    return ".".join(path_list)

def write(path, data):
    with open(path, "wt") as f:
        json.dump(data, f)
    



if __name__ == '__main__':
    if(len(sys.argv) < 2):
        print("usage: python3 convert_problem.py [filename]")
        exit(0)
    path = sys.argv[1]
    data = read_input(path)
    write(new_file(path), data)

    
