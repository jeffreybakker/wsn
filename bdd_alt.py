from dd.autoref import BDD, Function

from graph import Graph, Vertex


def alg_bdd_alt(graph: Graph, source: Vertex, target: Vertex):
    bdd = BDD()

    # Prepare the universe of variables in the BDD
    edges = list(set([e for v in graph.vertices for e in v.edges]))
    universe = {edges[i]: chr(i + 97) for i in range(len(edges))}
    for v in graph.vertices:
        universe[v] = str(v)

    for u in universe.values():
        bdd.declare(u)

    # Create a lookup table for finding the object correlating to a given name
    lookup = {v: k for (k, v) in universe.items()}

    # Define all sub-BDDs
    bdds = {source: bdd.true, target: bdd.false}
    for v in graph.vertices:
        if v == source or v == target:
            continue

        w = None
        for e in v.edges:
            other = e.get_other(v)

            current = (~bdd.var(universe[e]) & bdd.var(universe[other]))
            w = w | current if w else current

        bdds[v] = w

    for (v, tree) in bdds.items():
        name = universe[v]

        for n in v.neighbours:
            bdds[n] = bdd.let({name: tree}, bdds[n])

    influence = 0.0
    rates = {}

    bdd.declare('vertex')
    for v in graph.vertices:
        top = bdd.var('vertex') & (~bdd.var(universe[v]))

        for tree in bdds.values():
            top = top & tree

        rates[v] = evaluate(top, lookup)
        influence += rates[v] * v.households

    return influence, rates


def evaluate(top: Function, lookup):
    item = lookup[top.var] if top.var else None
    weight = 0.5 if isinstance(item, Vertex) or not item else item.weight

    hi = evaluate(top.high, lookup) if top.high and top.high.var else 1.0
    lo = evaluate(top.low, lookup) if top.low and top.low.var else 0.0

    return weight * hi + (1.0 - weight) * lo
