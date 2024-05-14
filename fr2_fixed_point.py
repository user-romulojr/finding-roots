from romu_math import *
from function_parser import substitute, infix_to_postfix

def fixed_point_method(data):
    relative_error = data["rerror"]
    num_iterations = 1000
    
    point = data["point"]
    iteration_func = infix_to_postfix(data["it-function"])

    COL_NUM = 4
    cur_error = 100

    iteration_table = [ ]
    label = [ "n", "x_n", "g(x_n)", "\epsilon_a" ]

    it = 0
    for it in range(len(label)):
        label[it] = "\\(" + label[it] + "\\)"
    
    iteration_table.append(label)

    # calculating the 0-th iteration
    base_case = [ None ] * COL_NUM
    base_case[0] = 0
    base_case[1] = point
    base_case[2] = substitute(point, iteration_func)
    base_case[3] = cur_error
    iteration_table.append(base_case)


    while(iteration_table[-1][-1] > relative_error and iteration_table[-1][0] < num_iterations):
        x = iteration_table[-1][2]
        y = substitute(x, iteration_func)

        prev_x = iteration_table[-1][1]
        ea = get_error(x, prev_x)
        
        it = iteration_table[-1][0] + 1
        cur_iteration = [ it, x, y, ea ]
        iteration_table.append(cur_iteration)


    for i in range(1,len(iteration_table)):
        iteration_table[i][-1] = my_round(iteration_table[i][-1], 2)
    iteration_table[1][-1] = "---"

    return iteration_table

