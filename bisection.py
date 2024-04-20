import math
from romu_math import *

# substituting x to the function
# INPUT HERE THE FUNCTION
def substitute(x):
    my_round(x, 5)
    ans = math.cos(x) - x * (math.e ** x)
    return my_round(ans, 5)

# calculates the slope of two points
def slope(x0, x1):
    rise = substitute(x0)-substitute(x1)
    run = x0-x1
    return rise/run

# calculating the next point
def next(x0, x1):
    my_round(x0, 5)
    my_round(x1, 5)
    ans = (x0 + x1) / 2
    return my_round(ans, 5)

def print_answer(answer):
    for iteration in answer:
        for j in range(1,7):
            iteration[j] = my_round(iteration[j], 5)
        iteration[-1] = my_round(iteration[-1], 2)
        print(iteration)

def bisection():
    # The CONSTANTS ( or the given values )
    relative_error = 0
    num_iterations = 15

    left = -5
    right = -3.5

    COL_NUM = 7

    cur_error = 100
    iteration_table = [ ]
    label = ["n", "a", "b", "x", "sgn[f(a)]", "sgn[f(p)]", "Ea"]
    iteration_table.append(label)
    # calculating the 0-th iteration
    base_case = [ None ] * COL_NUM
    base_case[0] = 0
    base_case[1] = left
    base_case[2] = right
    base_case[3] = next(left,right)
    base_case[4] = substitute(base_case[1])
    base_case[5] = substitute(base_case[3])
    base_case[6] = cur_error
    iteration_table.append(base_case)


    while(iteration_table[-1][-1] > relative_error and iteration_table[-1][0] < num_iterations):
        a = iteration_table[-1][1]
        b = iteration_table[-1][2]
        p = iteration_table[-1][3]

        fa = iteration_table[-1][4]
        fp = iteration_table[-1][5]

        if(sign(fa,fp)>0):
            a = p
        else:
            b = p

        it = iteration_table[-1][0] + 1
        p = next(a, b)
        fa = substitute(a)
        fp = substitute(p)
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
    
    return iteration_table