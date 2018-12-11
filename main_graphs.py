from graphs.models import Graph, Edge, Vertex
from graphs.shortest_paths import floyd_warshall, graph_to_matrix
import random


def main_dfs():
    g = Graph()

    a = Vertex('A')
    b = Vertex('B')
    c = Vertex('C')

    ab = Edge(a, b, 2)
    bc = Edge(b, c, 3)
    ac = Edge(a, c, 4)

    g.vertices.append(a)
    g.vertices.append(b)
    g.vertices.append(c)

    g.edges.append(ab)
    g.edges.append(bc)
    g.edges.append(ac)

    print(g)

    dot = g.to_graphviz()
    dot.render("images/test.gv")


def main_floyd_warshall():
    g = generate_random_graph(5, 5)

    dot = g.to_graphviz()
    dot.render("images/large-graph.gv")

    w = graph_to_matrix(g)

    print_matrix(w)

    d = floyd_warshall(g)

    print("Shortest Paths:")
    print_matrix(d)

    for i in range(len(g.vertices)):
        for j in range(len(g.vertices)):
            source = g.vertices[i]
            target = g.vertices[j]
            distance = d[i][j]
            print("{0} -> {1}'s shortest path is {2}".format(source, target, distance))



def print_matrix(w):
    for row in w:
        for cell in row:
            print("{:<5}".format(cell), end="")
        print("\n")


def generate_random_graph(num_vertices=10, num_edges=12, directed=False):
    g = Graph(directed)

    ascii_start = 65

    for i in range(num_vertices):
        v = Vertex(chr(i + ascii_start))
        g.vertices.append(v)

    while len(g.edges) < num_edges:
        source = pick_vertex(g)
        target = pick_vertex(g)

        if source == target:
            continue  # Skip if they're the same

        if g.contains_edge(source, target):
            continue

        e = Edge(source, target, 1)
        g.edges.append(e)

    return g


def pick_vertex(graph):
    index = random.randint(0, len(graph.vertices) - 1)
    return graph.vertices[index]


if __name__ == "__main__":
    # main_dfs()
    main_floyd_warshall()
