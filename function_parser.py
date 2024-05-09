from math import *
from romu_math import Stack


operator = "+-*/^()"
special_func = [ "sin", 'cos', "tan", "csc", "sec", "cot", "log"]
operations= { "(": 0 , ")": 1, "+":2 , "-": 2, "*": 3, "/": 3, "^" : 4}


def parse_function(func):
    result = [ ]

    i=0
    while i < len(func):
        if func[i] in operator:
            result.append(func[i])
        elif func[i].isdigit():
            left = i
            while i + 1 < len(func) and (func[i + 1].isdigit() or func[i+1] == "."):
                i += 1
            result.append(func[left : i + 1])
        elif func[i] == "x":
            if i > 0 and (result[-1][0].isdigit() or result[-1] == "e"):
                result.append("*")
            result.append(func[i])
        elif func[i] == "e":
            if i > 0 and result[-1] == "x":
                result.append("*")
            result.append(func[i])
        elif func[i : i + 2] == "ln":
            result.append(func[i : i + 2])
        elif func[i : i + 3] in special_func:
            result.append(func[i : i + 3])
        i += 1

    return result


def infix_to_postfix(func):
    func = parse_function(func)
    print(func)

    output = [ ]
    operator_stack = Stack()

    for i in func:
        if i[0].isdigit():
            output.append(i)
        elif i == "x" or i == "e":
            output.append(i)
        elif i in special_func:
            operator_stack.push(i)
        elif i == "(":
            operator_stack.push(i)
        elif i == ")":
            while operations[operator_stack.top()] != "(":
                output.append(operator_stack.top())
                operator_stack.pop()
            operator_stack.pop()
        elif i in operations:
            while not operator_stack.empty() and (not operator_stack.top() in operations or operations[i]<= operations[operator_stack.top()]):
                output.append(operator_stack.top())
                operator_stack.pop()
            operator_stack.push(i)

    while not operator_stack.empty():
        output.append(operator_stack.top())
        operator_stack.pop()     

    return output


def unary_operation(operator, value):
    if operator == "sin":
        return sin(value)
    if operator == "cos":
        return cos(value)
    if operator == "tan":
        return tan(value)
    if operator == "csc":
        return 1 / sin(value)
    if operator == "sec":
        return 1 / cos(value)
    if operator == "cot":
        return 1 / tan(value)
    if operator == "log":
        return log10(value)
    if operator == "ln":
        return log(value)


def binary_operation(operator, a, b):
    if b == "e":
        b = e
    if operator == "^":
        if a == "e":
            return exp(b)
        return a ** b
    if a == "e":
        a = e

    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "/":
        return a / b



def substitute(value, func):
    operand_stack = Stack()

    for i in func:
        if i[0].isdigit():
            operand_stack.push(float(i))
        elif i == "x":
            operand_stack.push(value)
        elif i == "e":
            operand_stack.push(i)
        elif i in operator:
            b = operand_stack.top()
            operand_stack.pop()

            a = operand_stack.top()
            operand_stack.pop()

            result = binary_operation(i, a, b)
            operand_stack.push(result)
        else:
            result = unary_operation(i, operand_stack.top())
            operand_stack.pop()
            operand_stack.push(result)
    
    return operand_stack.top()
