precision_error = 14

class Node:
    def __init__(self, value):
        self.value = value
        self.next= None
        
class Stack:
    def __init__(self):
        self.head= None
        self.tail= None
        
    def push(self, value):
        if self.head == None:
            node_1 = Node(value)
            self.head= node_1
            self.tail = node_1
        else:
            prev_head = self.head
            node_new= Node(value)
            self.head= node_new
            self.head.next = prev_head
    
    def pop(self):
        if self.head == None:
            return None
        else:
            prev_head= self.head
            new_head = self.head.next
            prev_head.next = None
            self.head = new_head
            
            return prev_head.value
        
    def top(self):
        if self.head== None:
            return None
        else:
            return self.head.value
    
    def empty(self):
        return self.head == None
        
def fix_error(num):
    negative = num < 0
    if negative:
        num *= -1

    base10 = 10 ** (precision_error+1)
    num = int(num * base10)
    if num % 10 >= 5:
        num += 10
    num = num // 10
    num /= base10 / 10

    if negative:
        num *= -1
    return num

def my_round(num, places):
    negative = num < 0
    if negative:
        num *= -1

    num = fix_error(num)

    base10 = 10 ** (places+1)
    num = int(num * base10)
    if num % 10 >= 5:
        num += 10
    num = num // 10
    num /= base10 / 10

    if negative:
        num *= -1
    return num

def sign(x0, x1):
    return (x0 < 0 and x1 < 0) or (x0 > 0 and x1 > 0)

def get_error(cur, prv):
    absolute_error = abs(cur-prv)
    ans = abs(absolute_error/cur) * 100
    return ans