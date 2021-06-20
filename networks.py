import random
from typing import Dict

from graph import Graph


def all_networks() -> Dict[str, Graph]:
    return {
        "lisandro": example_lisandro(),
        "simple": example_simple(),
        "complex": example_complex(),
        "surrounded": example_surrounded(),
        "middle": example_middle(),
        "triple": example_triple(),
        "combi": example_combi()

        # "campus-simple": example_campus_simple()

        # "rand50": example_random(50),
        # "rand25": example_random(25),
        # "rand10": example_random(10),
        # "rand5": example_random(5)
    }


def example_lisandro():
    g = Graph()

    network = g.create_vertex(0, "Network")
    a = g.create_vertex(300, "A")
    b = g.create_vertex(100, "Target")
    c = g.create_vertex(500, "C")

    network.create_edge(a, 0.0)
    network.create_edge(b, 0.0)
    a.create_edge(b, 0.2)
    a.create_edge(c, 0.4)
    b.create_edge(c, 0.9)

    return g


def example_simple():
    g = Graph()

    network = g.create_vertex(0, "Network")
    a = g.create_vertex(200, "A")
    b = g.create_vertex(500, "B")
    c = g.create_vertex(300, "C")
    d = g.create_vertex(400, "Target")

    network.create_edge(a, 0.0)
    network.create_edge(b, 0.0)
    a.create_edge(c, 0.8)
    b.create_edge(c, 0.4)
    c.create_edge(d, 0.25)

    return g


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


def example_surrounded():
    g = Graph()

    network = g.create_vertex(0, "Network")
    a = g.create_vertex(200, "A")
    b = g.create_vertex(500, "B")
    c = g.create_vertex(200, "C")
    d = g.create_vertex(400, "D")
    e = g.create_vertex(600, "E")
    f = g.create_vertex(800, "Target")

    network.create_edge(a, 0.0)
    network.create_edge(e, 0.0)
    a.create_edge(b, 0.6)
    a.create_edge(f, 0.4)
    b.create_edge(c, 0.7)
    c.create_edge(f, 0.2)
    c.create_edge(d, 0.5)
    d.create_edge(e, 0.4)
    e.create_edge(f, 0.9)

    return g


def example_middle():
    g = Graph()

    network = g.create_vertex(0, "Network")
    a = g.create_vertex(500, "A")
    b = g.create_vertex(400, "Target")
    c = g.create_vertex(900, "C")
    d = g.create_vertex(100, "D")

    network.create_edge(a, 0.0)
    network.create_edge(b, 0.0)
    a.create_edge(b, 0.5)
    b.create_edge(c, 0.2)
    c.create_edge(d, 0.9)

    return g


def example_triple():
    g = Graph()

    network = g.create_vertex(0, "Network")
    a = g.create_vertex(100, "A")
    b = g.create_vertex(100, "B")
    c = g.create_vertex(100, "C")
    d = g.create_vertex(100, "D")
    e = g.create_vertex(100, "Target")

    network.create_edge(a, 0.0)
    network.create_edge(b, 0.0)
    network.create_edge(c, 0.0)
    a.create_edge(e, 0.5)
    a.create_edge(d, 0.2)
    b.create_edge(d, 0.65)
    c.create_edge(d, 0.4)
    c.create_edge(e, 0.3)
    d.create_edge(e, 0.5)

    return g


def example_combi():
    g = Graph()

    network = g.create_vertex(0, "Network")
    a = g.create_vertex(100, "A")
    b = g.create_vertex(100, "Target")
    c = g.create_vertex(100, "C")
    d = g.create_vertex(100, "D")
    e = g.create_vertex(100, "E")
    f = g.create_vertex(100, "F")

    network.create_edge(a, 0.0)
    network.create_edge(b, 0.0)
    network.create_edge(c, 0.0)
    a.create_edge(b, 0.5)
    a.create_edge(d, 0.7)
    b.create_edge(c, 0.2)
    b.create_edge(e, 0.8)
    c.create_edge(f, 0.4)

    return g


def example_campus_simple():
    g = Graph()

    network = g.create_vertex(0, "Network")
    wbw = g.create_vertex(500, "WBW")
    zwembad = g.create_vertex(50, "Zwembad")
    matenweg = g.create_vertex(180, "Matenweg")
    campuslaan = g.create_vertex(240, "Campuslaan")
    calslaan = g.create_vertex(600, "Calslaan")
    box = g.create_vertex(200, "Box")
    sport = g.create_vertex(50, "Sport")
    spiegel = g.create_vertex(50, "Spiegel")
    sky = g.create_vertex(400, "Target")
    bastille = g.create_vertex(100, "Bastille")
    vrijhof = g.create_vertex(100, "Vrijhof")
    hogekamp = g.create_vertex(400, "Hogekamp")
    ono = g.create_vertex(500, "O&O")
    cubicus = g.create_vertex(200, "Cubicus")
    carre = g.create_vertex(300, "Carre")
    horst = g.create_vertex(300, "Horst")
    techno = g.create_vertex(200, "Technohal")

    network.create_edge(calslaan)
    network.create_edge(spiegel)
    network.create_edge(carre)

    calslaan.create_edge(campuslaan)
    calslaan.create_edge(spiegel)
    spiegel.create_edge(sport)
    spiegel.create_edge(bastille)
    spiegel.create_edge(ono)
    ono.create_edge(techno)
    ono.create_edge(vrijhof)
    ono.create_edge(carre)
    carre.create_edge(cubicus)
    carre.create_edge(horst)

    campuslaan.create_edge(matenweg)
    matenweg.create_edge(wbw)
    matenweg.create_edge(zwembad)
    matenweg.create_edge(box)
    box.create_edge(zwembad)
    box.create_edge(sport)
    sport.create_edge(sky)
    sky.create_edge(bastille)
    bastille.create_edge(vrijhof)
    vrijhof.create_edge(zwembad)
    vrijhof.create_edge(hogekamp)
    vrijhof.create_edge(cubicus)
    zwembad.create_edge(wbw)

    return g


def example_random(size):
    g = Graph()

    # Create source and target nodes
    network = g.create_vertex(0, "Network")
    target = g.create_vertex(random.randint(0, 10) * 10, "Target")

    # Generate vertices
    vertices = [g.create_vertex(random.randint(0, 10) * 10, chr(i + 65)) for i in range(size)]

    # Create edges
    for i in range(random.randint(2, 6)):
        network.create_edge(vertices[random.randint(0, len(vertices) - 1)], random.random())
        target.create_edge(vertices[random.randint(0, len(vertices) - 1)], random.random())

    for v in vertices:
        for i in range(random.randint(1, 5)):
            v.create_edge(vertices[random.randint(0, len(vertices) - 1)], random.random())

    return g
