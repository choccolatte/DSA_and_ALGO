class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v, c):
        self.adj_matrix[u][v] = c

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data
			
	def dfs(self, s, t, visited=None, path=None):
		if visited is None:
			visited = [False] * self.size
		if path is None:
			path = []

		visited[s] = True
		path.append(s)

		if s == t:
			return path

		for ind, val in enumerate(self.adj_matrix[s]):
			if not visited[ind] and val > 0:
				result_path = self.dfs(ind, t, visited, path.copy())
				if result_path:
					return result_path

		return None