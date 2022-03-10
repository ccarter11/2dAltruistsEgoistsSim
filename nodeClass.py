from numpy import double


class node:
    def __init__(self, node_type, payoff, willChange) -> None:
        if type(node_type)== 'str':
            self.node_type = node_type

        if type(payoff) == double:
            self.payoff= payoff 
        
        if type(willChange) == 'boolean':
            self.willChange = willChange

        self.edges =[]

        pass

    def updateType(self, newType):
        if (newType== "A" or newType=="E" or newType== "a" or newType=="e"):
            self.node_type= newType
        else:
            print("Invalid node type")

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

    
    




