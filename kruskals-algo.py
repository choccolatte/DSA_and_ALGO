class Graph:
    def __init__(self, size):
        self.size = size
        self.edges = [] # for storing edges as (weight, u, v)
        self.vertex_data = [''] * size # store vertex names

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.edges.append((weight, u, v)) # add edge with weight

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data