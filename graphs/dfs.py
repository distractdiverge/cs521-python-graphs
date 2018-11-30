from .models import Color


def dfs(graph):
    for vertex in graph.vertices:
        vertex.color = Color.White

    pass


def dfs_visit():
    pass