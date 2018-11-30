from enum import Enum
import graphviz


class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []

    def __repr__(self):
        print("<Graph NumVertices={0}, NumEdges={1}>".format(len(self.vertices), len(self.edges)))

    def __str__(self):
        result = "Vertices: \n"
        for vertex in self.vertices:
            result += "\t{0}\n".format(str(vertex))

        result += "\n"
        result += "Edges: \n"
        for edge in self.edges:
            result += "\t{0}\n".format(str(edge))

        return result

    def to_graphviz(self):
        dot = graphviz.Digraph(format="png", engine="neato")
        dot.node_attr.update(color='coral3', style='filled')

        for vertex in self.vertices:
            dot.node(vertex.name, fontcolor='linen')

        for edge in self.edges:
            dot.edge(edge.source.name, edge.target.name, str(edge.weight), len='1.50')

        return dot


class Vertex:
    def __init__(self, name):
        self.name = name
        self.color = None
        self.predecessor = None

    def __repr__(self):
        print("<Vertex name='{0}', color='{1}', predecessor='{2}'>".format(self.name, self.color, self.predecessor.name))

    def __str__(self):
        return self.name


class Edge:
    def __init__(self, source, target, weight=None):

        if source is None or target is None:
            raise ValueError("Both source and target must be non-Null")

        self.source = source
        self.target = target
        self.weight = weight

    def __repr__(self):
        print("<Edge '{0}'->'{1}', Weight: {2}>".format(self.source, self.target, self.weight))

    def __str__(self):
        return "{0}->{1} weight: ({2})".format(self.source.name, self.target.name, self.weight)


class Color(Enum):
    White = 0
    Grey = 1
    Black = 2

