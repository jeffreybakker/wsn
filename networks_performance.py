from graph import Graph, Vertex
from typing import Dict, List, Tuple

networks = {}


def performance_networks() -> Dict[str, Graph]:
    return networks


def base_graph(n) -> Tuple[Graph, List[Vertex]]:
    g = Graph()

    vertices = [
        g.create_vertex(100, "Network"),
        g.create_vertex(100, "Target")
    ]

    for i in range(2, n):
        vertices.append(g.create_vertex(100))

    return g, vertices


# First a dummy graph to make sure all code is in RAM
g, v = base_graph(3)
net = g.get_vertex("Network")
target = g.get_vertex("Target")

net.create_edge(v[2])
target.create_edge(v[2])

networks['dummy'] = g


##
# 3 VERTICES
##
# |V| = 3, |E| = 2
g, v = base_graph(3)
net = g.get_vertex("Network")
target = g.get_vertex("Target")

net.create_edge(v[2])
target.create_edge(v[2])

networks['3_2'] = g


# |V| = 3, |E| = 3
g, v = base_graph(3)
net = g.get_vertex("Network")
target = g.get_vertex("Target")

net.create_edge(v[2])
target.create_edge(v[2])
net.create_edge(target)

networks['3_3'] = g


##
# 4 VERTICES
##
# |V| = 4, |E| = 3
g, v = base_graph(4)
net = g.get_vertex("Network")
target = g.get_vertex("Target")

net.create_edge(v[2])
net.create_edge(v[3])
target.create_edge(v[2])

networks['4_3'] = g


# |V| = 4, |E| = 4
g, v = base_graph(4)
net = g.get_vertex("Network")
target = g.get_vertex("Target")

net.create_edge(v[2])
net.create_edge(v[3])
target.create_edge(v[2])
target.create_edge(v[3])

networks['4_4'] = g


# |V| = 4, |E| = 5
g, v = base_graph(4)
net = g.get_vertex("Network")
target = g.get_vertex("Target")

net.create_edge(v[2])
net.create_edge(v[3])
target.create_edge(v[2])
target.create_edge(v[3])
v[2].create_edge(v[3])

networks['4_5'] = g


# |V| = 4, |E| = 6
g, v = base_graph(4)
net = g.get_vertex("Network")
target = g.get_vertex("Target")

net.create_edge(v[2])
net.create_edge(v[3])
target.create_edge(v[2])
target.create_edge(v[3])
v[2].create_edge(v[3])
net.create_edge(target)

networks['4_6'] = g


##
# 5 VERTICES
##
# |V| = 5, |E| = 4
g, v = base_graph(5)
net = g.get_vertex("Network")
target = g.get_vertex("Target")

net.create_edge(v[2])
net.create_edge(v[3])
target.create_edge(v[2])
v[3].create_edge(v[4])

networks['5_4'] = g


# |V| = 5, |E| = 5
g, v = base_graph(5)
net = g.get_vertex("Network")
target = g.get_vertex("Target")

net.create_edge(v[2])
net.create_edge(v[3])
target.create_edge(v[2])
v[3].create_edge(v[4])
v[2].create_edge(v[3])

networks['5_5'] = g


# |V| = 5, |E| = 6
g, v = base_graph(5)
net = g.get_vertex("Network")
target = g.get_vertex("Target")

net.create_edge(v[2])
net.create_edge(v[3])
target.create_edge(v[2])
v[3].create_edge(v[4])
v[2].create_edge(v[3])
target.create_edge(v[4])

networks['5_6'] = g


# |V| = 5, |E| = 7
g, v = base_graph(5)
net = g.get_vertex("Network")
target = g.get_vertex("Target")

net.create_edge(v[2])
net.create_edge(v[3])
target.create_edge(v[2])
v[3].create_edge(v[4])
v[2].create_edge(v[3])
target.create_edge(v[4])
target.create_edge(v[3])

networks['5_7'] = g


##
# 6 VERTICES
##
# |V| = 6, |E| = 5
g, v = base_graph(6)
net = g.get_vertex("Network")
target = g.get_vertex("Target")

net.create_edge(target)
net.create_edge(v[2])
net.create_edge(v[3])
v[2].create_edge(v[4])
v[2].create_edge(v[5])

networks['6_5'] = g


# |V| = 6, |E| = 6
g, v = base_graph(6)
net = g.get_vertex("Network")
target = g.get_vertex("Target")

net.create_edge(target)
net.create_edge(v[2])
net.create_edge(v[3])
v[2].create_edge(v[4])
v[2].create_edge(v[5])
target.create_edge(v[4])

networks['6_6'] = g


# |V| = 6, |E| = 7
g, v = base_graph(6)
net = g.get_vertex("Network")
target = g.get_vertex("Target")

net.create_edge(target)
net.create_edge(v[2])
net.create_edge(v[3])
v[2].create_edge(v[4])
v[2].create_edge(v[5])
target.create_edge(v[4])
v[3].create_edge(v[5])

networks['6_7'] = g


# |V| = 6, |E| = 8
g, v = base_graph(6)
net = g.get_vertex("Network")
target = g.get_vertex("Target")

net.create_edge(target)
net.create_edge(v[2])
net.create_edge(v[3])
v[2].create_edge(v[4])
v[2].create_edge(v[5])
target.create_edge(v[4])
v[3].create_edge(v[5])
v[4].create_edge(v[5])

networks['6_8'] = g


# |V| = 6, |E| = 9
g, v = base_graph(6)
net = g.get_vertex("Network")
target = g.get_vertex("Target")

net.create_edge(target)
net.create_edge(v[2])
net.create_edge(v[3])
v[2].create_edge(v[4])
v[2].create_edge(v[5])
target.create_edge(v[4])
v[3].create_edge(v[5])
v[4].create_edge(v[5])
v[2].create_edge(v[3])

networks['6_9'] = g


# |V| = 6, |E| = 10
g, v = base_graph(6)
net = g.get_vertex("Network")
target = g.get_vertex("Target")

net.create_edge(target)
net.create_edge(v[2])
net.create_edge(v[3])
v[2].create_edge(v[4])
v[2].create_edge(v[5])
target.create_edge(v[4])
v[3].create_edge(v[5])
v[4].create_edge(v[5])
v[2].create_edge(v[3])
target.create_edge(v[2])

networks['6_10'] = g


##
# 7 VERTICES
##
# |V| = 7, |E| = 6
g, v = base_graph(7)
net = g.get_vertex("Network")
target = g.get_vertex("Target")

net.create_edge(target)
net.create_edge(v[2])
net.create_edge(v[3])
v[2].create_edge(v[4])
v[2].create_edge(v[5])
v[5].create_edge(v[6])

networks['7_6'] = g


# |V| = 7, |E| = 7
g, v = base_graph(7)
net = g.get_vertex("Network")
target = g.get_vertex("Target")

net.create_edge(target)
net.create_edge(v[2])
net.create_edge(v[3])
v[2].create_edge(v[4])
v[2].create_edge(v[5])
target.create_edge(v[4])
v[5].create_edge(v[6])

networks['7_7'] = g


# |V| = 7, |E| = 8
g, v = base_graph(7)
net = g.get_vertex("Network")
target = g.get_vertex("Target")

net.create_edge(target)
net.create_edge(v[2])
net.create_edge(v[3])
v[2].create_edge(v[4])
v[2].create_edge(v[5])
target.create_edge(v[4])
v[3].create_edge(v[5])
v[5].create_edge(v[6])

networks['7_8'] = g


# |V| = 7, |E| = 9
g, v = base_graph(7)
net = g.get_vertex("Network")
target = g.get_vertex("Target")

net.create_edge(target)
net.create_edge(v[2])
net.create_edge(v[3])
v[2].create_edge(v[4])
v[2].create_edge(v[5])
target.create_edge(v[4])
v[3].create_edge(v[5])
v[4].create_edge(v[5])
v[5].create_edge(v[6])

networks['7_9'] = g


# |V| = 7, |E| = 10
g, v = base_graph(7)
net = g.get_vertex("Network")
target = g.get_vertex("Target")

net.create_edge(target)
net.create_edge(v[2])
net.create_edge(v[3])
v[2].create_edge(v[4])
v[2].create_edge(v[5])
target.create_edge(v[4])
v[3].create_edge(v[5])
v[4].create_edge(v[5])
v[2].create_edge(v[3])
v[5].create_edge(v[6])

networks['7_10'] = g


# |V| = 7, |E| = 11
g, v = base_graph(7)
net = g.get_vertex("Network")
target = g.get_vertex("Target")

net.create_edge(target)
net.create_edge(v[2])
net.create_edge(v[3])
v[2].create_edge(v[4])
v[2].create_edge(v[5])
target.create_edge(v[4])
v[3].create_edge(v[5])
v[4].create_edge(v[5])
v[2].create_edge(v[3])
target.create_edge(v[2])
v[5].create_edge(v[6])

networks['7_11'] = g


##
# 8 VERTICES
##
# |V| = 8, |E| = 7
g, v = base_graph(8)
net = g.get_vertex("Network")
target = g.get_vertex("Target")

net.create_edge(target)
net.create_edge(v[2])
net.create_edge(v[3])
v[2].create_edge(v[4])
v[2].create_edge(v[5])
v[5].create_edge(v[6])
v[4].create_edge(v[7])

networks['8_7'] = g


# |V| = 8, |E| = 8
g, v = base_graph(8)
net = g.get_vertex("Network")
target = g.get_vertex("Target")

net.create_edge(target)
net.create_edge(v[2])
net.create_edge(v[3])
v[2].create_edge(v[4])
v[2].create_edge(v[5])
target.create_edge(v[4])
v[5].create_edge(v[6])
v[4].create_edge(v[7])

networks['8_8'] = g


# |V| = 8, |E| = 9
g, v = base_graph(8)
net = g.get_vertex("Network")
target = g.get_vertex("Target")

net.create_edge(target)
net.create_edge(v[2])
net.create_edge(v[3])
v[2].create_edge(v[4])
v[2].create_edge(v[5])
target.create_edge(v[4])
v[3].create_edge(v[5])
v[5].create_edge(v[6])
v[4].create_edge(v[7])

networks['8_9'] = g


# |V| = 8, |E| = 10
g, v = base_graph(8)
net = g.get_vertex("Network")
target = g.get_vertex("Target")

net.create_edge(target)
net.create_edge(v[2])
net.create_edge(v[3])
v[2].create_edge(v[4])
v[2].create_edge(v[5])
target.create_edge(v[4])
v[3].create_edge(v[5])
v[4].create_edge(v[5])
v[5].create_edge(v[6])
v[4].create_edge(v[7])

networks['8_10'] = g


# |V| = 8, |E| = 11
g, v = base_graph(8)
net = g.get_vertex("Network")
target = g.get_vertex("Target")

net.create_edge(target)
net.create_edge(v[2])
net.create_edge(v[3])
v[2].create_edge(v[4])
v[2].create_edge(v[5])
target.create_edge(v[4])
v[3].create_edge(v[5])
v[4].create_edge(v[5])
v[2].create_edge(v[3])
v[5].create_edge(v[6])
v[4].create_edge(v[7])

networks['8_11'] = g


# |V| = 8, |E| = 12
g, v = base_graph(8)
net = g.get_vertex("Network")
target = g.get_vertex("Target")

net.create_edge(target)
net.create_edge(v[2])
net.create_edge(v[3])
v[2].create_edge(v[4])
v[2].create_edge(v[5])
target.create_edge(v[4])
v[3].create_edge(v[5])
v[4].create_edge(v[5])
v[2].create_edge(v[3])
target.create_edge(v[2])
v[5].create_edge(v[6])
v[4].create_edge(v[7])

networks['8_12'] = g
