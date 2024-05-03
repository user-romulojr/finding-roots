operator = "+-*/^()"
special_func = [ "sin", "cos", "tan", "csc", "sec", "cot", "log"]

test = "69x + log(x) * 35"

def make_list(func):
    result = [ ]

    i=0
    while i < len(func):
        if func[i] in operator:
            result.append(func[i])
        elif func[i].isdigit():
            left = i
            while i + 1 < len(func) and func[i + 1].isdigit():
                i += 1
            result.append(func[left : i + 1])
        elif func[i] == "x":
            if i > 0 and result[-1][0].isdigit():
                result.append("*")
            result.append(func[i])
        elif func[i] == "e":
            result.append(func[i])
        elif func[i : i + 2] == "ln":
            result.append(func[i : i + 2])
        elif func[i : i + 3] in special_func:
            result.append(func[i : i + 3])
        i += 1

    return result

print(make_list(test))