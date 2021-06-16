from typing import List
from time import time

from graph import Graph, Vertex, Edge

from dd.autoref import BDD, Function


def example_complex():
    g = Graph()

    network = g.create_vertex(0, "Network")
    a = g.create_vertex(100, "A")
    b = g.create_vertex(100, "B")
    c = g.create_vertex(100, "C")
    d = g.create_vertex(100, "D")
    e = g.create_vertex(100, "Target")

    network.create_edge(a, 0.0)
    network.create_edge(b, 0.0)
    a.create_edge(b, 0.5)
    a.create_edge(c, 0.5)
    b.create_edge(d, 0.5)
    c.create_edge(d, 0.5)
    c.create_edge(e, 0.5)
    d.create_edge(e, 0.5)

    return g


start = time()

graph = example_complex()
network = graph.get_vertex("Network")
target = graph.get_vertex("Target")

bdd = BDD()
edges = {}
for e in list(set([e for v in graph.vertices for e in v.edges])):
    edges[str(e)] = e
    bdd.declare(str(e))


def traverse(v: Vertex, visited: List[Vertex]) -> Function:
    res = None

    for e in v.edges:
        next = e.get_other(v)
        if next in visited:
            continue

        term = bdd.var(str(e))

        expr = traverse(next, visited + [v])
        expr = expr.implies(term) if expr else term

        res = res | expr if res else expr

    return res


top = traverse(target, [network])


def terminate(failed: List[Edge]):
    # Compute the set of directly impacted vertices
    disabled = set()
    queue = [target]

    while len(queue) > 0:
        v = queue.pop()
        if v in disabled:
            continue

        disabled.add(v)

        for e in v.edges:
            if e not in failed:
                continue

            next = e.get_other(v)
            queue.append(next)

    cutoff = set(graph.vertices)
    queue = [network]

    while len(queue) > 0:
        v = queue.pop()
        if v not in cutoff:
            continue
        if v in disabled:
            continue

        cutoff.remove(v)

        for n in v.neighbours:
            queue.append(n)

    return sum([v.households for v in cutoff])


def evaluate(top: Function, failed: List[Edge]):
    edge = edges[top.var]

    hi = evaluate(top.high, failed + [edge]) + terminate(failed + [edge]) if top.high.var else terminate(failed + [edge])
    lo = evaluate(top.low, failed) if top.low.var else terminate(failed)

    return edge.weight * hi + (1.0 - edge.weight) * lo


influence = evaluate(top, [])
print("Total influence: {}".format(influence))

end = time()
print("That took {}s".format(end - start))

bdd.collect_garbage()
bdd.dump('bdd.pdf', roots=[top])
