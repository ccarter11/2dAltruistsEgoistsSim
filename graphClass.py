class graph: 
   
    def __init__(self, nodes=[]):
        self.nodes = nodes

    def add_node(self, val):
        newNode = node(nType, 0, False)
        self.nodes.append(newNode)

    def add_edge(self, node1, node2):
        node1.edges.append(node2)
        node2.edges.append(node1)