from random import randint

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.current = None

    def __iter__(self):
        self.current = self.head
        while self.current:
            yield self.current.data
            self.current = self.current.next

    def __str__(self):
        values = [str(x) for x in self]
        return ' -> '.join(values)

    def __len__(self):
        count = 0
        self.current = self.head
        while self.current != None:
            count += 1
            self.current = self.current.next
        return count

    def add_node(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            node = Node(data)
            self.current = self.head
            while self.current.next != None:
                self.current = self.current.next
            self.current.next = node

    def delete_node(self, data):
        if self.head.data == data:
            self.head = self.head.next
        else:
            self.current = self.head
            while self.current.next != None:
                next_node = self.current.next
                if next_node.data == data:
                    self.current.next = next_node.next
                    break
                self.current = self.current.next

    def generate(self, n, min_value, max_value):
        self.head = None
        for i in range(n):
            self.add_node(randint(min_value, max_value))

    def get_node_data(self):
        data = []
        self.current = self.head
        while self.current != None:
            data.append(self.current.data)
            self.current = self.current.next
        return data