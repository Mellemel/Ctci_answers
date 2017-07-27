class EmptyStackError(Exception):
    pass

class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    
    def pop(self):
        if self.top == None:
            raise EmptyStackError("Stack is empty.")
        item = self.top
        self.top = self.top.next
        return item

    def push(self, item):
        new_top = StackNode(item)
        new_top.next = self.top
        self.top = new_top

    def peek(self):
        if self.top == None:
            raise EmptyStackError
        return self.top.data

    def isEmpty(self):
        return self.top == None