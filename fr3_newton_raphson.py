from romu_math import *
from function_parser import substitute, infix_to_postfix

def substitute_derivative(x, func):
    return substitute(x, func)

def next(x, func, derivative_func):
    my_round(x, 5)
    ans = x - (substitute(x, func) / substitute_derivative(x, derivative_func))
    return my_round(ans, 5)

def newton_raphson_method(data):
    relative_error = data["rerror"]
    point = data["point"]
    func = infix_to_postfix(data["function"])
    derivative_func = infix_to_postfix(data["derivative-function"])

    COL_NUM = 5
    cur_error = 100

    iteration_table = [ ]
    label = ["n", "x_n", "f(x_n)", "f'(x_n)", "\epsilon_a"]

    it = 0
    for it in range(len(label)):
        label[it] = "\\(" + label[it] + "\\)"

    iteration_table.append(label)

    # calculating the 0-th iteration
    base_case = [ None ] * COL_NUM
    base_case[0] = 0
    base_case[1] = point
    base_case[2] = substitute(point, func)
    base_case[3] = substitute_derivative(point, derivative_func)
    base_case[4] = cur_error
    iteration_table.append(base_case)


    while(iteration_table[-1][-1] > relative_error):
        prev_x = iteration_table[-1][1]
        x = next(prev_x, func, derivative_func)
        y = substitute(x, func)
        dy = substitute_derivative(x, derivative_func)

        ea = get_error(x, prev_x)
        
        it = iteration_table[-1][0] + 1
        cur_iteration = [ it, x, y, dy, ea ]
        iteration_table.append(cur_iteration)

    for i in range(1,len(iteration_table)):
        iteration_table[i][-1] = my_round(iteration_table[i][-1], 2)
        print(iteration_table[i])
    iteration_table[1][-1] = "---"

    return iteration_table
