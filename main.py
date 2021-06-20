from tabulate import tabulate
import threading
from time import time

import networks
import networks_performance

import basic
import bdd
import bdd_alt
import naive
import naive_optimized
import search

PERFORMANCE_TEST = False
TIME_LIMIT = False

algorithms = {
    "Naive": naive.naive_wsn,
    "Naive Cache": naive_optimized.alg_naive_opt,
    "Basic": basic.alg_basic,
    "BDD": bdd.alg_bdd,
    "Search": search.alg_search
}

results = {v: {} for (k, v) in algorithms.items()}


def measure(alg, graph, source, target):
    global result

    start = time()

    influence, rates = alg(graph, source, target)

    end = time()

    # Generate and save the result
    res = "{:.2f} in {:.2f} ms".format(influence, (end - start) * 1000)

    if PERFORMANCE_TEST:
        results[alg][graph] += (end - start) * 1000
    else:
        results[alg][graph] = res

    return res


data = []
nets = networks_performance.performance_networks() if PERFORMANCE_TEST else networks.all_networks()

for (name, graph) in nets.items():
    source = graph.get_vertex("Network")
    target = graph.get_vertex("Target")

    if TIME_LIMIT:
        threads = {}
        for (label, algorithm) in algorithms.items():
            results[algorithm][graph] = 0.0
            for i in range(5 if PERFORMANCE_TEST else 1):
                threads[label] = threading.Thread(target=measure, args=(algorithm, graph, source, target))
                threads[label].start()
                try:
                    threads[label].join(30.0)
                except RuntimeError:
                    threads[label].exit()

        data.append(
            [name] + ['{:.3f}'.format(results[v][graph] / 5.0) if PERFORMANCE_TEST else results[v][graph] if graph in results[v].keys() else "D.N.F." for (k, v) in algorithms.items()])
    else:
        data.append([
            name,
            measure(naive.naive_wsn, graph, source, target),
            measure(naive_optimized.alg_naive_opt, graph, source, target),
            measure(basic.alg_basic, graph, source, target),
            measure(bdd.alg_bdd, graph, source, target),
            measure(search.alg_search, graph, source, target)
        ])

print(tabulate(data, headers=["Network"] + [k for k in algorithms.keys()]))
