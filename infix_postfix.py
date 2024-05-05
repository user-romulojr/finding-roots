from romu_math import Stack as st
a= "1+2*3-4"
#result dapat 
'''123*+4-'''
special_func=["sin","cos","tan","csc","sec","cot" ]
operations= { "(": 0 , ")": 1, "+":2 , "-": 2, "*": 3, "/": 3}
output=[ ]
s= st()
def disp_output():
    for i in a:
        if i.isdigit():
            output.append(i)
        elif i in special_func:
            s.push(i)
        elif s.empty():
            s.push(i)
        elif operations[i] == 0:
            s.push(i)
        elif operations[i] == 1:
            while operations[s.top()]!=0:
                output.append(s.top())
                s.pop()
            s.pop()
        elif operations[i] > operations[s.top()]:
            s.push(i)
        elif  operations[i] <= operations[s.top()]:
            while not s.empty() and operations[i]<= operations[s.top()]:
                output.append(s.top())
                s.pop()
            s.push(i)
    while not s.empty():
        output.append(s.top())
        s.pop()            
    return output              
print(disp_output())
