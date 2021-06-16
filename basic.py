from graph import Graph, Vertex, Edge
from time import time
from typing import List, Union, Set


def alg_basic(graph: Graph, source: Vertex, target: Vertex):
    rates = {}
    rates[target] = 1.0

    for v in graph.vertices:
        # But skip the target node or the network node
        if v == target or v == source:
            continue

        deps = dependencies(v, source, target, [])
        paths = find_paths(v, target, deps if deps is not None else [], [])

        # rate = 0.0
        # chances = [r for (_, r, _) in paths]
        # for i in range(len(chances)):
        #     rate += chances[i]
        #     for j in range(i + 1, len(chances)):
        #         rate -= chances[i] * chances[j]
        #
        # rate += math.prod([c for c in chances if c > 0.0])
        # rates[v] = rate

        rate = 1.0
        for (_, r, _) in paths:
            rate *= 1 - r
            # rate = rate + r #- rate * r
        rates[v] = 1 - rate

    influence = sum([k.households * v for (k, v) in rates.items()])

    return influence, rates


def dependencies(current: Vertex, source: Vertex, target: Vertex, visited: List["Vertex"], start=True):
    """
    Generates, for a given start vertex, the list of dependencies. Considering that the target will be cut-off from the
    network's water source, cutting off any of the returned dependencies will result in the given vertex being cut off
    from the network's water source as well.
    :param current: the vertex to consider
    :param source: the network's water source
    :param target: the node that is the "target"
    :param visited: the list of already visited vertices
    :return: a list of dependencies for the given current vertex
    """
    # The target vertex cannot be one of the dependencies since it is being cut off from the network already
    if current == target:
        return None
    # We have found the network's water source, so start constructing the list of dependencies
    elif current == source:
        return [source]

    res = []
    visited += [current]

    # For all neighbours,
    for n in current.neighbours:
        # That have not been visited yet
        if n in visited:
            continue

        # Recursively construct the list of dependencies
        deps = dependencies(n, source, target, visited, False)
        if deps is not None:
            res += deps
            visited += deps

        visited += [n]

    return (res if start else res + [current]) if len(res) > 0 else None


def find_paths(current: Vertex, target: Vertex, dependencies: List["Vertex"], visited: List["Vertex"]):
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
        for (final, rate, path) in find_paths(next, target, dependencies, visited + [current]):
            if final:
                # This route has been terminated already
                res.append((final, rate, path))
            else:
                # Set final if this node is in one of the dependencies
                res.append((current in dependencies, rate * e.weight, path + [e]))

    return res


if __name__ == "__main__":
    import networks

    start = time()

    graph = networks.example_lisandro()
    source = graph.get_vertex("Network")
    target = graph.get_vertex("Target")

    influence, rates = alg_basic(graph, source, target)

    end = time()

    print("Total influence: {}".format(influence))
    for (vertex, rate) in rates.items():
        if vertex == source or vertex == target:
            continue

        print("{}: {}".format(vertex, rate))

    print("")
    print("That took {}s".format(end - start))
