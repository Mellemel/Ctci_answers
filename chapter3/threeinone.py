from stack import Stack, EmptyStackError

class StacksFullError(Exception):
    pass

class MultiStack:
    def __init__(self, stack_size):
        self.stacks = [Stack() for _ in range(3)]
        self.stack_size = stack_size
        self.push_exit = 0

    def pop(self, stack_num):
        if self.stacks[stack_num].top == None:
            raise EmptyStackError(f'{stack_num} is empty')
        return self.stacks[stack_num].pop()

    def push(self, stack_num, item):
        if self.stacks[stack_num] == self.stack_size:
            stack_num = (stack_num + 1) % len(self.stacks)
            self.push_exit += 1
            if self.push_exit == 3:
                raise StacksFullError
            stack_num = self.push(stack_num, item)
        else:
            self.stacks[stack_num].push(item)
        self.push_exit = 0
        return stack_num

    def peek(self, stack_num):
        if self.stacks[stack_num].top == None:
            raise EmptyStackError
        return self.stacks[stack_num].top.data

    def isEmpty(self, stack_num):
        return self.stacks[stack_num].top == None
