from dd.autoref import BDD, Function
from typing import List
from time import time

import basic
from graph import Graph, Vertex


def alg_bdd(graph: Graph, source: Vertex, target: Vertex):
    rates = {}

    bdd = BDD()
    edges = list(set([e for v in graph.vertices for e in v.edges]))
    edges = {edges[i]: chr(i + 97) for i in range(len(edges))}
    legend = {v: k for (k, v) in edges.items()}

    for (_, v) in edges.items():
        bdd.declare(v)

    influence = target.households

    # Compute the failure rates for all vertices in the graph
    for v in graph.vertices:
        # But skip the target node or the network node
        if v == target or v == source:
            continue

        deps = basic.dependencies(v, source, target, [])
        paths = compute(v, target, deps if deps is not None else [], [source])

        statement = None
        for (_, _, path) in paths:
            p = ' & '.join([edges[e] for e in path])
            if statement is None:
                statement = '({})'.format(p)
            else:
                statement += ' | ({})'.format(p)

        expr = bdd.add_expr(statement)
        rate = evaluate(expr, legend)

        influence += v.households * rate
        rates[v] = rate

    return influence, rates


def compute(current: Vertex, target: Vertex, dependencies: List["Vertex"], visited: List["Vertex"]):
    """
    Returns the different paths from `current` to `target` and their corresponding failure rates
    :param current: the starting node
    :param target: the target node
    :param dependencies: the list of dependencies of the starting node, see `dependencies(...)`
    :param visited: the list of already visited vertices
    :return: a list of paths to the target node and their corresponding failure rates
    """
    # If we have found the target, then start constructing the route
    if current == target:
        return [(False, 1.0, [])]

    res = []

    # Otherwise consider all of the neighbours for a depth-first search
    for e in current.edges:
        # Get the neighbour from the edge
        next = e.get_other(current)
        if next in visited:
            continue

        # And recursively consider and construct the paths
        for (final, rate, path) in compute(next, target, dependencies, visited + [current]):
            if final:
                # This route has been terminated already
                res.append((final, rate, path))
            else:
                # Set final if this node is in one of the dependencies
                res.append((current in dependencies, rate * e.weight, path + [e]))

    return res


def evaluate(top: Function, legend={}):
    edge = legend[top.var]

    hi = evaluate(top.high, legend) if top.high.var else 1.0
    lo = evaluate(top.low, legend) if top.low.var else 0.0

    return edge.weight * hi + (1.0 - edge.weight) * lo


if __name__ == '__main__':
    import networks

    start = time()

    graph = networks.example_lisandro()
    source = graph.get_vertex("Network")
    target = graph.get_vertex("Target")

    influence, rates = alg_bdd(graph, source, target)

    end = time()

    print("Total influence: {}".format(influence))
    for (vertex, rate) in rates.items():
        if vertex == source or vertex == target:
            continue

        print("{}: {}".format(vertex, rate))

    print("")
    print("That took {}s".format(end - start))
