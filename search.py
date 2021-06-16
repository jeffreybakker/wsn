from dd.autoref import BDD, Function
import math
from typing import List

from graph import Graph, Vertex


def alg_search(graph: Graph, source: Vertex, target: Vertex):
    dependencies = {v: set() for v in graph.vertices}

    queue = [(source, source)]
    visited = set()
    while len(queue) > 0:
        v, prev = queue.pop(0)
        visited.add(v)

        for n in v.neighbours:
            if n == source or n == target or n == prev:
                continue

            if n not in visited:
                queue.append((n, v))

            # if v != source and v != target:
            dependencies[n].add(v)

    bdd = BDD()
    edges = list(set([e for v in graph.vertices for e in v.edges]))
    legend = {str(e): e for e in edges}

    for e in edges:
        bdd.declare(str(e))

    def terminate(failed: List[Vertex]):
        res = {}
        for (v, deps) in dependencies.items():
            if not deps:
                continue

            if v in failed:
                continue

            if not all([d in failed for d in deps]):
                continue

            failed = failed + [v]
            res[v] = bdd.true

        if res:
            result, failed = terminate(failed)
            for (k, v) in result.items():
                res[k] = v

        return res, failed

    def compute(v: Vertex, failed: List[Vertex]) -> dict[Vertex, Function]:
        failed = failed + [v]
        bdds, failed = terminate(failed)
        bdds[v] = bdd.true

        for n in v.neighbours:
            if n in failed:
                continue

            edge = bdd.var(str(v.get_edge(n)))
            res = compute(n, failed)

            for (k, tree) in res.items():
                if k in bdds.keys() and bdds[k] != bdd.true:
                    bdds[k] = bdds[k] | (edge & tree)
                else:
                    bdds[k] = edge & tree

        return bdds

    def evaluate(tree: Function):
        if tree == bdd.true:
            return 1.0

        edge = legend[tree.var]

        hi = 1.0 if tree.high == bdd.true else evaluate(tree.high)
        lo = 0.0 if tree.low == bdd.false else evaluate(tree.low)

        return edge.weight * hi + (1.0 - edge.weight) * lo

    trees = compute(target, [])
    influence = 0.0
    rates = {}

    # bdd.collect_garbage()

    for (v, tree) in trees.items():
        # bdd.dump("{}.pdf".format(v.label), roots=[tree])
        rates[v] = evaluate(tree)
        influence += rates[v] * v.households

    return influence, rates
