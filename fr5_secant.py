from romu_math import *
from function_parser import substitute, infix_to_postfix


def slope(x0, x1, func):
    rise = substitute(x0, func) - substitute(x1, func)
    run = x0 - x1
    return rise / run

def next(x0, x1, func):
    my_round(x0, 5)
    my_round(x1, 5)
    ans = x1 - (substitute(x1, func) / slope(x1, x0, func))
    return my_round(ans, 5)

def secant_method(data):
    relative_error = data["rerror"]
    num_iterations = 1000

    left = data["minval"]
    right = data["maxval"]
    
    func = infix_to_postfix(data["function"])
    
    COL_NUM = 4
    cur_error = 100

    iteration_table = [ ]
    label = ["n", "x_n", "f(x_n)", "\epsilon_a"]

    it = 0
    for it in range(len(label)):
        label[it] = "\\(" + label[it] + "\\)"

    iteration_table.append(label)
    # calculating the 0-th iteration
    base_case1 = [ None ] * COL_NUM
    base_case2 = [ None ] * COL_NUM

    base_case1[0] = 0
    base_case1[1] = left
    base_case1[2] = substitute(left, func)
    base_case1[3] = cur_error
    iteration_table.append(base_case1)

    base_case2[0] = 1
    base_case2[1] = right
    base_case2[2] = substitute(right, func)
    base_case2[3] = cur_error
    iteration_table.append(base_case2)


    while(iteration_table[-1][-1] > relative_error):
        x0 = iteration_table[-2][1]
        x1 = iteration_table[-1][1]
        x2 = next(x0, x1, func)

        y2 = substitute(x2, func)
        ea = get_error(x2, x1)
        
        it = iteration_table[-1][0] + 1
        cur_iteration = [ it, x2, y2, ea ]
        print(cur_iteration)
        iteration_table.append(cur_iteration)

    for i in range(1,len(iteration_table)):
        iteration_table[i][-1] = my_round(iteration_table[i][-1], 2)
        print(iteration_table[i])
    iteration_table[1][-1] = "---"
    iteration_table[2][-1] = "---"

    return iteration_table
