from graph import Graph
from queue import Queue

def find_path():
    graph = Graph(10)
    q = Queue(maxsize=-1)
    q.put(graph.getSt)
    first = graph.