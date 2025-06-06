class Graph:
    # ...
    def add_edge(self, u, v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = 1

    # ...
    def dfs_util(self, v, visited, recStack):
        visited[v] = True
        recStack[v] = True
        print("Current vertex: ", self.vertex_data[v])

        for i in range(self.size):
            if self.adj_matrix[v][i] == 1:
                if not visited[i]:
                    if self.dfs_util(i, visited, recStack):
                        return True
                elif recStack[i]:
                    return True

        recStack[v] = False
        return False

    def is_cyclic(self):
        visited = [False] * self.size
        recStack = [False] * self.size

        for i in range(self.size):
            if not visited[i]:
                print() # new line
                if self.dfs_util(i, visited, recStack):
                    return True
        return False

g = Graph(7)

# ...
g.add_edge(3, 0)  # D -> A
g.add_edge(0, 2)  # A -> C
g.add_edge(2, 1)  # C -> B
g.add_edge(2, 4)  # C -> E
g.add_edge(1, 5)  # B -> F
g.add_edge(4, 0)  # E -> A
g.add_edge(2, 6)  # C -> G

g.print_graph()

print("Graph has cycle: ", g.is_cyclic())