import math
from romu_math import *

# The CONSTANTS ( or the given values )
relative_error = 1
point = 0.025

COL_NUM = 5

# substituting x to the function
# INPUT HERE THE FUNCTION
def substitute(x):
    my_round(x, 5)
    ans = 6 * x + 2 * math.log(x, math.e) - 400
    return my_round(ans, 5)


def substitute_derivative(x):
    my_round(x, 5)
    ans = 2 / x + 6
    return my_round(ans, 5)


# calculating the next point
def next(x):
    my_round(x, 5)
    ans = x-(substitute(x)/substitute_derivative(x))
    return my_round(ans, 5)



cur_error = 100
iteration_table = [ ]
label = ["n", "x(n)", "f(x(n))", "f'(x(n))", "Ea"]
iteration_table.append(label)

# calculating the 0-th iteration
base_case = [ None ] * COL_NUM

base_case[0] = 0
base_case[1] = point
base_case[2] = substitute(point)
base_case[3] = substitute_derivative(point)
base_case[4] = cur_error
iteration_table.append(base_case)


while(iteration_table[-1][-1] > relative_error):
    prev_x = iteration_table[-1][1]
    x = next(prev_x)
    y = substitute(x)
    dy = substitute_derivative(x)

    ea = get_error(x, prev_x)
    
    it = iteration_table[-1][0] + 1
    cur_iteration = [ it, x, y, dy, ea ]
    iteration_table.append(cur_iteration)

for i in range(1,len(iteration_table)):
    iteration_table[i][-1] = my_round(iteration_table[i][-1], 2)
    print(iteration_table[i])