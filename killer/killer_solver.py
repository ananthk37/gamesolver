from constraint import AllDifferentConstraint, ExactSumConstraint, Problem

def solve(init_board, groups):
    killer_problem = Problem()

    killer_problem.addVariables(list(range(81)), list(range(1, 10)))

    #game constraints
    for i in range(9):
        #row constraints
        killer_problem.addConstraint(AllDifferentConstraint(), [j for j in range(9 * i, 9 * (i + 1))])
        #column constraints
        killer_problem.addConstraint(AllDifferentConstraint(), [j for j in range(i, 81, 9)])
    for i in range(3):
        for j in range(3):
            start = i * 27 + j * 3
            vals = [start, start + 1, start + 2,
                    start + 9, start + 10, start + 11,
                    start + 18, start + 19, start + 20]
            killer_problem.addConstraint(AllDifferentConstraint(), vals)
    
    for variable in init_board.keys():
        killer_problem.addConstraint(
            lambda var, val=init_board[variable]: var==val, [variable])
    for group_sum, group in groups:
        killer_problem.addConstraint(ExactSumConstraint(group_sum), group)
    
    solution = killer_problem.getSolution()
    solution_str = ""
    for i in range(81):
        solution_str += str(solution[i])
    
    return solution_str



def console_print(board):
    """
        Print a given board to the console.
    """
    for i in range(9):
        start = i * 9
        print(*list(board[start:start + 9]), sep='|')
        if i % 3 == 2:
            print(*(['-'] * 17), sep='')
