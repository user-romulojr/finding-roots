from romu_math import *
from function_parser import substitute, infix_to_postfix

def slope(x0, x1, func):
    rise = substitute(x0, func) - substitute(x1, func)
    run = x0 - x1
    return rise / run

def next(x0, x1, func):
    my_round(x0, 5)
    my_round(x1, 5)
    ans = x1-(substitute(x1, func)/slope(x1, x0, func))
    return my_round(ans, 5)

def regula_falsi_method(data):
    relative_error = data["rerror"]
    num_iterations = 1000

    left = data["minval"]
    right = data["maxval"]
    
    func = infix_to_postfix(data["function"])

    COL_NUM = 8
    cur_error = 100

    iteration_table = [ ]
    label = ["n", "x_n", "x_{n+1}", "x_{n+2}", "f(x_n)", "f(x_{n+1})", "f(x_{n+2})", "\epsilon_a"]

    it = 0
    for it in range(len(label)):
        label[it] = "\\(" + label[it] + "\\)"

    iteration_table.append(label)

    # calculating the 0-th iteration
    base_case = [ None ] * COL_NUM
    base_case[0] = 0
    base_case[1] = left
    base_case[2] = right
    base_case[3] = next(left,right, func)
    base_case[4] = substitute(base_case[1], func)
    base_case[5] = substitute(base_case[2], func)
    base_case[6] = substitute(base_case[3], func)
    base_case[7] = cur_error
    iteration_table.append(base_case)

    while(iteration_table[-1][-1] > relative_error and iteration_table[-1][0] < num_iterations):
        a = iteration_table[-1][1]
        b = iteration_table[-1][2]
        p = iteration_table[-1][3]

        if sign(p,b)>0:
            a = p
        else:
            b = p

        it = iteration_table[-1][0] + 1
        p = next(a, b, func)
        fa = substitute(a, func)
        fb = substitute(b, func)
        fp = substitute(p, func)
        ea = get_error(p, iteration_table[-1][3])

        cur_iteration = [ it, a, b, p, fa, fb, fp, ea ]
        iteration_table.append(cur_iteration)

    for i in range(1,len(iteration_table)):
        iteration_table[i][-1] = my_round(iteration_table[i][-1], 2)
        print(iteration_table[i])
    iteration_table[1][-1] = "---"

    return iteration_table