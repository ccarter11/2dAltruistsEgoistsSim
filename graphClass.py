#import node class from nodeClass.py
from nodeClass import node
import random

class graph: 
   
    def __init__(self, nodes=[]):
        self.nodes = nodes #set array of nodes 

    def add_node(self,label, nType): #add a new node to graph with base attributes
        newNode = node(label,nType, 0, False) 
        self.nodes.append(newNode) 

    def add_edge(self, node1, node2): #connect two nodes by adding them to eachothers edge array 
        if node1 not in node2.edges:
            node2.edges.append(node1)
        if node2 not in node1.edges:
            node1.edges.append(node2)

    
    def remove_edge(self, node1, node2): #remove edge 
        node1.edges.remove(node2)
        node2.edges.remove(node1)
    
    # def get_node(self, node_id):  #
    #     for node in self.nodes:
    #         if node.id == node_id:
    #             return node
    #     return None

    #Check if node is connected to another
    def is_connected(self, node1, node2):
        if node1 in node2.edges:
            return True
        else:
            return False

    # def get_neighbors(self, node): 
    #     return node.edges

    def connectNodes(self): #set random edges in graph 
        numEdges = random.randint(len(self.nodes),(len(self.nodes)**2)) # pick a random number of edges 
        
        for i in range(len(self.nodes)-1): # start with line of nodes to make sure that all agents are connected 
             self.add_edge(self.nodes[i], self.nodes[i+1])
             numEdges-=1
        while numEdges>0: # if there are some additional edges available, use them to connect random nodes 
            node1,node2 = random.randint(0,len(self.nodes)-1), random.randint(0,len(self.nodes)-1)#choose two random nodes
            if (self.nodes[node1] != self.nodes[node2]): # if not the same node 
                self.add_edge(self.nodes[node1], self.nodes[node2]) #try to add edge
                if self.nodes[node1] in self.nodes[node2].edges: #if success
                    numEdges-=1 #reduce number of edges 

            
        
            
        