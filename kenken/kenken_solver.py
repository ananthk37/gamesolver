from constraint import Problem, ExactSumConstraint, AllDifferentConstraint, Constraint
from ..utils import ExactProductConstraint

def sum_constraint(result):
    return ExactSumConstraint(result)

def diff_constraint(result):
    return lambda a, b: a - b == result or b - a == result

def prod_constraint(result):
    return ExactProductConstraint(result)

def quot_constraint(result):
    return lambda a, b: a / b == result or b / a == result




def solve(board_size, board, groups):
    kenken_problem = Problem()
    kenken_problem.addVariables(list(range(board_size ** 2)), list(range(1, 1 + board_size)))

    for i in range(board_size):
        kenken_problem.addConstraint(AllDifferentConstraint(), [j for j in range(board_size * i, board_size * (i + 1))])
        kenken_problem.addConstraint(AllDifferentConstraint(), [j for j in range(i, board_size ** 2, board_size)])

    for variable in board.keys():
        kenken_problem.addConstraint(
            lambda var, val=board[variable]: var == val, [variable]
        )

    #groups -- group_op, group_result, group
    ops_to_constraints = {
        '+': sum_constraint,
        '-': diff_constraint,
        '*': prod_constraint,
        '/': quot_constraint
    }
    for group_op, group_result, group in groups:
        kenken_problem.addConstraint(ops_to_constraints[group_op](group_result), group)

    solution = kenken_problem.getSolution()
    solution_str = ""
    for i in range(board_size ** 2):
        solution_str += str(solution[i])
    
    return solution_str
    