from stack import Stack, EmptyStackError

class MinStack(Stack):
    def __init__(self):
        super()

    def min(self):
        if self.top == None:
            raise EmptyStackError
        runner = self.top
        min_data = None
        while runner != None:
            if min_data == None:
                min_data = runner.data
                continue
            if runner.data < min_data:
                min_data = runner.data
            runner = runner.next
        return min_data