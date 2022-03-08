#import node class from nodeClass.py
from nodeClass import node

class graph: 
   
    def __init__(self, nodes=[]):
        self.nodes = nodes

    def add_node(self, nType):
        newNode = node(nType, 0, False)
        self.nodes.append(newNode)

    def add_edge(self, node1, node2):
        if node1 not in node2.edges:
            node2.edges.append(node1)
        if node2 not in node1.edges:
            node1.edges.append(node2)
    
    def remove_edge(self, node1, node2):
        node1.edges.remove(node2)
        node2.edges.remove(node1)
    
    def get_node(self, node_id):
        for node in self.nodes:
            if node.id == node_id:
                return node
        return None

    #Check if node is connected to another
    def is_connected(self, node1, node2):
        if node1 in node2.edges:
            return True
        else:
            return False