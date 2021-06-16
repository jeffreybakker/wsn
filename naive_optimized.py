import math

from graph import Graph, Vertex
import naive


def alg_naive_opt(graph: Graph, source: Vertex, target: Vertex):
    # First create a list of all edges in the graph
    edges = list(set([e for v in graph.vertices for e in v.edges]))
    rates = {v: 0.0 for v in graph.vertices}

    cache = {}

    for i in range(2 ** len(edges)):
        # Generate the set of failed edges
        failed = [edges[j] for j in range(len(edges)) if (i >> j) & 1 > 0]
        chance = math.prod([e.weight if e in failed else 1.0 - e.weight for e in edges])

        # Get the set of directly impacted nodes
        vertices = naive.failed_vertices(target, failed)

        # Check cache if this case has been computed yet
        cid = str([str(v) for v in vertices])
        if cid in cache:
            impacted = cache[cid]
            for v in impacted:
                rates[v] += chance

            continue

        # Then compute which vertices are still reachable
        reached = naive.reachable(source, vertices)

        # Compute the absolute list of impacted vertices
        impacted = [v for v in graph.vertices if v not in reached]
        for v in impacted:
            rates[v] += chance

        # Finally, save the result in the cache
        cache[cid] = impacted

    influence = sum([k.households * v for (k, v) in rates.items()])

    return influence, rates
