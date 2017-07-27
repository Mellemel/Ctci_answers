class EmptyQueueError(Exception):
    pass

class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
    
    def add(item):
        new_node = QueueNode(item)
        if self.last == None and self.first == None:
            self.first = self.last = new_node
        else:
            self.last.next = new_node
            self.last = self.last.next

    def remove():
        if self.first == None:
            raise EmptyQueueError
        data = self.first
        self.first = self.first.next
        return data

    def peek():
        if self.first == None:
            raise EmptyQueueError
        return self.first.data

    def isEmpty():
        return self.first == None