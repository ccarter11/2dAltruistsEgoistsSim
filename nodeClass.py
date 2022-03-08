from numpy import double


class node:
    def __init__(self, node_type, payoff, willChange) -> None:
        if type(node_type)== Str:
            self.node_type = node_type

        if type(payoff) == double:
            self.payoff= payoff 
        
        if type(willChange) == boolean:
            self.willChange = willChange

        pass

    def updateType(self, newType):
        if (newType== "A" or newType=="E" or newType== "a" or newType=="e"):
            self.node_type= newType
        else:
            #return error message
    def updatePayoff(self, newPayoff):
        for each node in graph:
            if self.neighbor:
                self.payoff= self.payoff + newPayoff

    def updateChange(self, change):
        





