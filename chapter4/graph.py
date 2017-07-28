from random import randint


class Node():
    def __init__(self):
        self.visited = False
        self.adjacent = []


class Graph():
    def __init__(self, max_nodes):
        self.max_nodes = max_nodes
        self.total_edges = 0
        self.nodes = []
        self.start = None
        self.end = None
        self._generate()

    def _generate(self):
        self.nodes = [Node() for _ in range(self.max_nodes)]
        start = randint(0, self.max_nodes - 1)
        end = start
        while start == end:
            end = randint(0, self.max_nodes - 1)
        self.start = self.nodes[start]
        self.end = self.nodes[end]
        for node in self.nodes:
            rand_num_of_adj_nodes = randint(1, self.max_nodes)
            for _ in range(rand_num_of_adj_nodes):
                rand_index = randint(0, self.max_nodes - 1)
                other_node = self.nodes[rand_index]
                if node != other_node and other_node not in node.adjacent:
                    node.adjacent.append(other_node)

    def get_start_node(self):
        return self.start

    def get_end_node(self):
        return self.end


graph = Graph(10)
