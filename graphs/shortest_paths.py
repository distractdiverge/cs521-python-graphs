import math


def floyd_warshall(graph):

    # Construct the W matrix and D matrix
    weights = graph_to_matrix(graph)

    n = len(weights)  # Number of Rows

    distance = weights.copy()

    for k in range(n):
        # distance = [[math.inf for x in range(n)] for y in range(n)]
        for i in range(n):
            for j in range(n):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    return distance


def graph_to_matrix(graph):
    num_vertices = len(graph.vertices)
    w = [[math.inf for j in range(num_vertices)] for i in range(num_vertices)]

    # Take in a graph (edges & vertices) and create a 2-d matrix of weights
    for i in range(num_vertices):
        v1 = graph.vertices[i]
        for j in range(num_vertices):
            v2 = graph.vertices[j]

            if v1 == v2:
                w[i][j] = 0

            edge = graph.find_edge(v1, v2)
            if edge is not None:
                w[i][j] = edge.weight

    return w
