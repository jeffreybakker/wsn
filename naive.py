from typing import List
import math

from graph import Graph, Vertex, Edge


def naive_wsn(graph: Graph, network: Vertex, target: Vertex):
    # First create a list of all edges in the graph
    edges = list(set([e for v in graph.vertices for e in v.edges]))
    rates = {v: 0.0 for v in graph.vertices}

    for i in range(2 ** len(edges)):
        # Generate the set of failed edges
        failed = [edges[j] for j in range(len(edges)) if (i >> j) & 1 > 0]

        # Get the set of directly impacted nodes
        vertices = failed_vertices(target, failed)
        reached = reachable(network, vertices)

        # Compute the absolute list of impacted vertices
        impacted = [v for v in graph.vertices if v not in reached]

        chance = math.prod([e.weight if e in failed else 1.0 - e.weight for e in edges])
        for v in impacted:
            rates[v] += chance

    influence = sum([k.households * v for (k, v) in rates.items()])

    return influence, rates


def failed_vertices(target: Vertex, edges: List[Edge]) -> List[Vertex]:
    visited = []
    queue = [target]

    while len(queue) > 0:
        next = queue.pop()
        if next in visited:
            continue

        visited.append(next)

        for e in next.edges:
            if e not in edges:
                continue

            other = e.get_other(next)
            queue.append(other)

    return visited


def reachable(network: Vertex, visited: List[Vertex]) -> List[Vertex]:
    visited = visited + [network]

    res = [network]

    for v in network.neighbours:
        if v in visited:
            continue

        res += reachable(v, visited)

    return res
