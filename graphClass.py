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
    
    
    #Check if node is connected to another
    def is_connected(self, node1, node2):
        if node1 in node2.edges:
            return True
        else:
            return False

   
#assigns random edges in graph 
    def connectNodes(self): 
        numEdges = random.randint(len(self.nodes),(len(self.nodes)**2)) 
        
        for i in range(len(self.nodes)-1): # start with line of nodes to make sure that all agents are connected 
             self.add_edge(self.nodes[i], self.nodes[i+1])
             numEdges-=1
        while numEdges>0: # if there are additional edges available, use them to connect random agents  
            node1,node2 = random.randint(0,len(self.nodes)-1), random.randint(0,len(self.nodes)-1)
            if (self.nodes[node1] != self.nodes[node2]): 
                self.add_edge(self.nodes[node1], self.nodes[node2]) #try to add edge
                if self.nodes[node1] in self.nodes[node2].edges: #if success
                    numEdges-=1 #reduce number of edges 

            
        
            
        