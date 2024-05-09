from romu_math import *
from function_parser import substitute, infix_to_postfix


def next(x0, x1):
    my_round(x0, 5)
    my_round(x1, 5)
    ans = (x0 + x1) / 2
    return my_round(ans, 5)


def bisection_method(data):
    relative_error = data["rerror"]
    num_iterations = 1000

    left = data["minval"]
    right = data["maxval"]
    
    func = infix_to_postfix(data["function"])


    COL_NUM = 7
    cur_error = 100.0

    iteration_table = [ ]
    label = ["n", "a", "b", "x", "sgn[f(a)]", "sgn[f(p)]", "Ea"]
    iteration_table.append(label)

    # calculating the 0-th iteration
    base_case = [ None ] * COL_NUM
    base_case[0] = 0
    base_case[1] = left
    base_case[2] = right
    base_case[3] = next(left,right)
    base_case[4] = substitute(base_case[1], func)
    base_case[5] = substitute(base_case[3], func)
    base_case[6] = cur_error
    iteration_table.append(base_case)


    while iteration_table[-1][-1] > relative_error and iteration_table[-1][0] < num_iterations:
        a = iteration_table[-1][1]
        b = iteration_table[-1][2]
        p = iteration_table[-1][3]

        fa = iteration_table[-1][4]
        fp = iteration_table[-1][5]

        if sign(fa,fp) > 0:
            a = p
        else:
            b = p

        it = iteration_table[-1][0] + 1
        p = next(a, b)
        fa = substitute(a, func)
        fp = substitute(p, func)
        ea = get_error(p, iteration_table[-1][3])

        cur_iteration = [ it, a, b, p, fa, fp, ea ]
        iteration_table.append(cur_iteration)

    for i in range(1,len(iteration_table)):
        for j in range(4,6):
            if iteration_table[i][j] < 0:
                iteration_table[i][j] = "-"
            else:
                iteration_table[i][j] = "+"
        iteration_table[i][-1] = my_round(iteration_table[i][-1], 2)
    iteration_table[1][-1] = "---"
    
    return iteration_table