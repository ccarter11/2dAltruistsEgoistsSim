


class node:
    def __init__(self, label, node_type, payoff, willChange): #label never changes, node_type may change, payoff and willChange change mid epoch but are reset each time
        self.label= label #keeps track of unique nodes/ agents 
        
        self.node_type = node_type #keeps track of whether the agent is altruist of egoist 

        
        self.payoff= payoff #keeps track of agent payoff for each epoch 
        
       
        self.willChange = willChange #keeps track of whether or not the node will change in the next epoch 

        self.edges =[] #keeps track of neighboring agents 

        pass

    def updateType(self, newType):#set/changes node type 
        self.node_type= newType
        

    def updatePayoff(self, newPayoff):#set/changes agent payoff
        self.payoff += newPayoff

    def updateChange(self, change):#set/changes will change status
        self.willChange = change        

    def getType(self):#gets type value 
        return self.node_type

    def getPayoff(self):#get payoff value 
        return self.payoff

    def getChange(self):#get will change condition 
        return self.willChange

    def getNeighbors(self):#get array of neighboring agent  
        return self.edges

    def getLabel(self):#get agent label 
        return self.label 

    
    




