from numpy import double


class node:
    def __init__(self, label, node_type, payoff, willChange) -> None: #label never changes, node_type may change, payoff and willChange change mid epoch but are reset each time
        self.label= label 
        
        self.node_type = node_type

        
        self.payoff= payoff 
        
       
        self.willChange = willChange

        self.edges =[]

        pass

    def updateType(self, newType):
        self.node_type= newType
        

    def updatePayoff(self, newPayoff):
        self.payoff += newPayoff

    def updateChange(self, change):
        self.willChange = change        

    def getType(self):
        return self.node_type

    def getPayoff(self):
        return self.payoff

    def getChange(self):
        return self.willChange

    def getNeighbors(self):
        return self.edges

    def getLabel(self):
        return self.label 

    
    




