class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

class GraphNode(Node):
    def __init__(self, value=None):
        super().__init__(value)
        self.edges = LinkedList()

class Edge:
    def __init__(self, source, destination, weight=None, directed=True):
        self.source = source
        self.destination = destination
        self.weight = weight
        self.directed = directed

class Graph:
    def __init__(self, directed=True):
        self.nodes = {}
        self.directed = directed

    def add_node(self, value):
        if value not in self.nodes:
            self.nodes[value] = GraphNode(value)
        return self.nodes[value]

    def add_edge(self, source_value, destination_value, weight=None):
        source_node = self.add_node(source_value)
        destination_node = self.add_node(destination_value)
        new_edge = Edge(source_node, destination_node, weight, self.directed)
        source_node.edges.append(new_edge)
        if not self.directed:
            reverse_edge = Edge(destination_node, source_node, weight, self.directed)
            destination_node.edges.append(reverse_edge)

    def __iter__(self):
        for node_value in self.nodes:
            yield self.nodes[node_value]

    def print_graph(self):
        for node in self:
            edges = []
            current_edge = node.edges.head
            while current_edge:
                edge = current_edge.value
                edges.append(f"({edge.source.value} -> {edge.destination.value}){' ' + str(edge.weight) if edge.weight is not None else ''}")
                current_edge = current_edge.next
            print(f"Node {node.value}: " + ", ".join(edges))