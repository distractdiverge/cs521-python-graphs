from graphs.models import Graph, Edge, Vertex


def main():
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


if (__name__ == "__main__"):
    main()
