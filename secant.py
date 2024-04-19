import math
from romu_math import *

# The CONSTANTS ( or the given values )
relative_error = 0.02
left = 4.2
right = 5.5

COL_NUM = 4

# substituting x to the function
# INPUT HERE THE FUNCTION
def substitute(x):
    my_round(x, 5)
    ans = 1.25 * (x ** 3)  - 2.9375 * (x ** 2) - 71.375 * x + 73.0625
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
    ans = x1-(substitute(x1)/slope(x1,x0))
    return my_round(ans, 5)

def print_answer(answer):
    for iteration in answer:
        for j in range(1,7):
            iteration[j] = my_round(iteration[j], 5)
        iteration[-1] = my_round(iteration[-1], 2)
        print(iteration)



cur_error = 100
iteration_table = [ ]
label = ["n", "x(n)", "f(x(n))", "Ea"]
iteration_table.append(label)
# calculating the 0-th iteration
base_case1 = [ None ] * COL_NUM
base_case2 = [ None ] * COL_NUM

base_case1[0] = 0
base_case1[1] = left
base_case1[2] = substitute(left)
base_case1[3] = cur_error
iteration_table.append(base_case1)

base_case2[0] = 1
base_case2[1] = right
base_case2[2] = substitute(right)
base_case2[3] = cur_error
iteration_table.append(base_case2)


while(iteration_table[-1][-1] > relative_error):
    x0 = iteration_table[-2][1]
    x1 = iteration_table[-1][1]
    x2 = next(x0, x1)

    y2 = substitute(x2)
    ea = get_error(x2, x1)
    
    it = iteration_table[-1][0] + 1
    cur_iteration = [ it, x2, y2, ea ]
    print(cur_iteration)
    iteration_table.append(cur_iteration)

for i in range(1,len(iteration_table)):
    iteration_table[i][-1] = my_round(iteration_table[i][-1], 2)
    print(iteration_table[i])
