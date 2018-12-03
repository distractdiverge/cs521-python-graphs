from graphs.models import Graph, Edge, Vertex
from dynamic.common_sequences import lcs_length


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


def main_lcs():
    X = "abc123"
    Y = "abc1234"

    max_lcs = lcs_length(X, Y)

    print("Longest Commmon Sequence: {0}".format(max_lcs))

if (__name__ == "__main__"):
    # main_dfs()
    main_lcs()
