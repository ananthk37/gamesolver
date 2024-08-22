from constraint import AllDifferentConstraint, Problem

def solve(init_board):
    """
        Solves sudoku problem using constraint module. Constructs
        problem from initial board stored as dictionary.
    """
    sudoku_problem = Problem()
    ##define vsars --> init vals here?
    sudoku_problem.addVariables(list(range(81)), list(range(1, 10)))

    #game constraints
    for i in range(9):
        #row constraints
        sudoku_problem.addConstraint(AllDifferentConstraint(), [j for j in range(9 * i, 9 * (i + 1))])
        #column constraints
        sudoku_problem.addConstraint(AllDifferentConstraint(), [j for j in range(i, 81, 9)])
    for i in range(3):
        for j in range(3):
            start = i * 27 + j * 3
            vals = [start, start + 1, start + 2,
                    start + 9, start + 10, start + 11,
                    start + 18, start + 19, start + 20]
            sudoku_problem.addConstraint(AllDifferentConstraint(), vals)
    
    for variable in init_board.keys():
        sudoku_problem.addConstraint(
            lambda var, val=init_board[variable]: var==val, [variable])

    solution_str = ""
    solution = sudoku_problem.getSolution()
    if solution:
        for i in range(81):
            solution_str += str(solution[i])

    return solution_str

def test_board():
    """
        Return test board
    """
    return "040100050107003960520008000000000017000906800803050620090060543600080700250097100"

def to_dict(init_board):
    board_dict = {}
    for i, val in enumerate(init_board):
        if val != '0':
            board_dict[i] = int(val)
    return board_dict


def console_print(board):
    """
        Print a given board to the console.
    """
    for i in range(9):
        start = i * 9
        print(*list(board[start:start + 9]), sep='|')
        if i % 3 == 2:
            print(*(['-'] * 17), sep='')

if __name__ == '__main__':
    board = test_board()
    console_print(board)
    board = to_dict(board)
    solution = solve(board)
    print()
    console_print(solution)
    pass