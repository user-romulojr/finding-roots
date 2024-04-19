import openpyxl
import math
from romu_math import *

# The CONSTANTS ( or the given values )
relative_error = -1
num_iterations = 27

point = 3

COL_NUM = 4

# substituting x to the function
# INPUT HERE THE FUNCTION
# ans1 = (math.log(x, math.e) - 4) / x + 4
# ans2 = (math.log(x, math.e) ** (1/2)) + 2
# ans3 = (math.log(x, math.e) + 4 * x - 4) ** (1/2)
def substitute(x):
    my_round(x, 5)  
    ans = math.e ** ((x-2) ** 2)
    return my_round(ans, 5)



cur_error = 100
iteration_table = [ ]
label = ["n", "x(n)", "g(x(n))", "Ea"]
iteration_table.append(label)

# calculating the 0-th iteration
base_case = [ None ] * COL_NUM
base_case[0] = 0
base_case[1] = point
base_case[2] = substitute(point)
base_case[3] = cur_error
iteration_table.append(base_case)


while(iteration_table[-1][-1] > relative_error and iteration_table[-1][0] < num_iterations):
    x = iteration_table[-1][2]
    y = substitute(x)
    
    prev_x = iteration_table[-1][1]
    ea = get_error(x, prev_x)
    
    it = iteration_table[-1][0] + 1
    cur_iteration = [ it, x, y, ea ]
    iteration_table.append(cur_iteration)


for i in range(1,len(iteration_table)):
    iteration_table[i][-1] = my_round(iteration_table[i][-1], 10)
    print(iteration_table[i])

'''
file_path = "C:/Users/Romulo Ramos/Documents/NUMERICAL METHODS/regula_falsi.csv"
with open(file_path, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(iteration_table)
'''

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Fixed-Point"

for row in iteration_table:
    ws.append(row)

excel_file_path = "C:/Users/Romulo Ramos/Documents/NUMERICAL METHODS/fixed-point.xlsx"
wb.save(excel_file_path)
