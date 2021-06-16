from typing import List, Dict


class GraphError(Exception):
    pass


class Graph(object):
    def __init__(self):
        self._vertices = {}

        self._next_label = 0

    def create_vertex(self, households=0, label=None) -> "Vertex":
        v = Vertex(self, households, label)
        self._vertices[v.label] = v
        return v

    def del_vertex(self, vertex: "Vertex"):
        del self._vertices[vertex.label]

    def get_vertex(self, label) -> "Vertex":
        return self._vertices[label]

    def next_label(self):
        res = self._next_label
        self._next_label += 1
        return res

    @property
    def vertices(self) -> List["Vertex"]:
        return [v for (k, v) in self._vertices.items()]


class Vertex(object):
    def __init__(self, graph: Graph, households=0, label=None):
        if label is None:
            label = graph.next_label()

        self._graph = graph
        self._households = households
        self._label = label

        self._incidence = {}

    def __repr__(self) -> str:
        return 'Vertex("{}", {}, #{})'.format(self.label, self.households, len(self._incidence))

    def __str__(self) -> str:
        return self.label

    def create_edge(self, to: "Vertex", weight=1.0):
        """
        Creates an edge between this vertex and the given vertex.
        :param to: the other vertex
        :param weight: the weight (or failure probability) of the edge
        :return: the newly created edge
        """
        edge = Edge(self, to, weight)
        self._incidence[to] = edge
        to._incidence[self] = edge
        return edge

    def get_edge(self, to: "Vertex"):
        """
        Retrieves the edge from this vertex to the given vertex.
        :param to: the other vertex
        :return: the edge if it exists, `None` otherwise
        """
        if to not in self._incidence:
            return None

        return self._incidence[to]

    def remove_edge(self, edge: "Edge"):
        """
        Removes the edge from this (and the other) vertex's incidence.
        :param edge: the edge to remove
        """
        other = edge.get_other(self)
        del self._incidence[other]
        del other._incidence[self]

    def is_neighbour(self, other: "Vertex"):
        """
        Checks whether the given vertex is a neighbour of this vertex.
        :param other: the other vertex
        :return: `true` if there exists an edge from this vertex to the other vertex
        """
        return other in self._incidence

    @property
    def edges(self) -> List["Edge"]:
        return [v for (k, v) in self._incidence.items()]

    @property
    def graph(self) -> "Graph":
        return self._graph

    @property
    def households(self):
        return self._households

    @property
    def incidence(self) -> Dict["Vertex", "Edge"]:
        return self._incidence

    @property
    def label(self):
        return self._label

    @property
    def neighbours(self):
        return [k for (k, v) in self._incidence.items()]


class Edge(object):
    def __init__(self, tail: Vertex, head: Vertex, weight=0.5):
        """
        Creates an edge from a given tail pointing to a given head. In the case of an undirected graph, the order of
        these two doesnt matter.
        :param tail: the originating vertex
        :param head: the target vertex
        :param weight: the weight (or failure probability) of the vertex
        """
        self._tail = tail
        self._head = head
        self._weight = weight

    def __repr__(self) -> str:
        return "({}, {})".format(str(self.head), str(self.tail))

    def __str__(self) -> str:
        return self.__repr__()

    def is_incident(self, vertex: Vertex):
        """
        Checks whether the given vertex is either the head or the tail of this edge.
        :param vertex: the vertex to check
        :return: `true` if the vertex is equal to either the head or the tail of this edge
        """
        return vertex == self.head or vertex == self.tail

    def get_other(self, vertex: Vertex):
        """
        Given either the head or the tail, will return the tail or the head respectively
        :param vertex: the initial vertex
        :return:
        """
        if vertex == self.head:
            return self.tail
        elif vertex == self.tail:
            return self.head

        raise GraphError('Given vertex is neither on the head or tail of this edge')

    @property
    def tail(self):
        return self._tail

    @property
    def head(self):
        return self._head

    @property
    def weight(self):
        return self._weight
