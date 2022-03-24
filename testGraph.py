import matplotlib.pyplot as plt
import numpy as np

#import variable value from AltruistsEgoists.py
from AltruistsEgoists import altruistEgoistSim2D


def calcEpoch(self):#uses calcPayoff to determine if nodes will change type 

		self.reset()
		self.calcPayoff() #initialize this epoch's node payoffs

		before=[]
		after = []
		for node in self.simGraph.nodes: 
			altruistPayoff= 0  #track the payoff of the respective types neighboring each node 
			egoistPayoff = 0
			numAlt = 0 
			numEgo = 0
		
			#initialize based on current node type
			if node.getType()== 'A': 
				numAlt+= 1 
				altruistPayoff+= node.getPayoff()
			else: 
				numEgo+= 1 
				egoistPayoff+= node.getPayoff() 

			#check type and payoff of neighbors to determine which type "looks" best to this node 
			for neighbor in node.edges:
				if neighbor.getType()== 'A':
					numAlt+=1
					altruistPayoff += neighbor.getPayoff()
				else:
					numEgo+=1
					egoistPayoff +=neighbor.getPayoff()
					
			if numAlt == 0:#cant divide by zero
				numAlt=1
			if numEgo == 0:
				numEgo = 1 
			avgAltPO = altruistPayoff/numAlt
			avgEgoPO = egoistPayoff/numEgo 
			print(node.getLabel(), node.getType(),'ALT', avgAltPO, 'EGO', avgEgoPO)


			if ((avgAltPO>avgEgoPO) and node.getType() == 'E') or ((avgAltPO<avgEgoPO) and node.getType()=='A') :
				node.updateChange(True) 
		
			before.append(node.getType())
			print(node.getLabel(), node.getChange())
		self.returnNumAlt()	
		# for node in self.simGraph.nodes:
		# 	print(node.getType())

		#change all nodes' type accordingly
		self.changeNodeType()

		for node in self.simGraph.nodes:
		#print(node.getLabel() , node.getType())
			after.append(node.getType())
		print(before)
		print(after)

result = []
test1 = altruistEgoistSim2D(20,.1,.25)

# print(test1.getnodes)
# print(test1.getEdges)
result = test1.runSim(10)

def  runSim(self,  epochs):
    #Calls calc epoch 
    for i in range(epochs): 
        self.calcEpoch()
    print(self.data)
    result = self.data
    return self.data
    #Value for y and index for x

    # 
#print(result)


x = [0] * len(result)
y = [0] * len(result)

for i in range(0, len(result)):
    x[i] = i+1
    y[i] = result[i]

print("Size of x: ", len(x))
print("Size of y: ", len(y))
print("Size of result: ", len(result))

# make the data
np.random.seed(5)

# size and color:
sizes = np.random.uniform(15, 80, len(x))
colors = np.random.uniform(15, 80, len(x))
print("X:", x)
print("Y:", y)
# plot
fig, ax = plt.subplots()

ax.scatter(x, y)

ax.set(xlim=(0, result[0]), xticks=np.arange(0, len(result)+5),
       ylim=(0, result[1]), yticks=np.arange(0, max(result)+5))

plt.show()