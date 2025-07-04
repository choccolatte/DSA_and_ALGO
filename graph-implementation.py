vertexData = ['A', 'B', 'C', 'D']

adjacency_matrix = [
    [0, 1, 1, 1], # edges for A
    [1, 0, 1, 0], # edges for B
    [1, 1, 0, 0], # edges for C
    [1, 0, 0, 0] # edges for D
]

def print_adjacency_matrix(matrix):
    print("\nAdjacency Matrix: ")
    for row in matrix:
        print(row)

print('vertexData:', vertexData)
print_adjacency_matrix(adjacency_matrix)

# printing graph's connections
def print_connections(matrix, vertices):
    print("\nConnections for each vertex:")
    for i in range(len(vertices)):
        print(f"{vertices[i]}:", end="")
        for j in range(len(vertices)):
            if matrix[i][j]:  # if there is a connection
                print(vertices[j], end=" ")
        print() # prints new line
        