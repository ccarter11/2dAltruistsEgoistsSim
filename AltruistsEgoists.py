
from graphClass import graph
from nodeClass import node
import random

class altruistEgoistSim2D:
#…atributes… 
	def __init__(self, numNodes, probAltruist, altruismCost):
		#self.nodes = numNodes 
		#self.pAlt= probAltruist
		nodes = []
		simGraph = graph(nodes)
		for i in range(numNodes):
			#change based on user input probability
			nType = random.randint(0,1)
			if nType == 0:
				nType = 'A'
			else:
				nType = 'E'
			simGraph.add_node(nType)
			simGraph.connectNodes(simGraph)
			#self.getnodes = simGraph.nodes
			isEdges =[]
			#set random number of edges (and random conections) s.t. numNodes <|E| < numNodes**2 
			for node in simGraph.nodes:
				if len(node.edges)>0:
					isEdges.append(True)
			#self.getEdges = isEdges
		self.simGraph = simGraph
		self.cost = -altruismCost
		self.data=[]
		# print(self.simGraph.nodes)
		# print(len(self.simGraph.nodes))
				

				

		
	#def printNodesEdges():

	def returnNumAlt(self):
		numAlts = 0 
		for node in self.simGraph.nodes:
			if node.getType()=='A':
				numAlts+=1
		self.data.append(numAlts)
	
	

	#probably need to change simGraph references to self.simGraph... 
	def calcPayoff(self, simGraph):
		#for each node in the simGraph, check the type of each neighbor and increment payoff accordingly
		for node in simGraph.nodes:
			if node.getType()== 'A':
				node.updatePayoff(self.cost)
			for neighbor in node.edges: 
				if neighbor.getType()== 'A':
					node.updatePayoff(1)

	def changeNodeType(self):
		for node in self.simGraph.nodes:
			if node.willChange()==True:
				if node.getType()== 'A':
					node.updateType('E')
				if node.getType()== 'E': 
					node.updateType('A')

	def calcEpoch(self):#uses calcPayoff to determine if nodes will change type 

		#dont think im calling this function properly....
		self.calcPayoff(self.simGraph) #initialize this epoch's node payoffs

		
		for node in self.simGraph.nodes: 
			altruistPayoff= 0  
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
					
			
			avgAltPO = altruistPayoff/numAlt
			avgEgoPO = egoistPayoff/numEgo 

			if (avgAltPO>avgEgoPO and node.getType() == 'E') or (avgAltPO<avgEgoPO and node.getType=='A') :
				node.updateChange(True) 
			else:
				node.updateChange(False)
			
		#change all nodes' type accordingly
		self.returnNumAlt()
		self.changeNodeType()

	def  runSim(self,  epochs):
		#Calls calc epoch 
		for i in range(epochs): 
			self.calcEpoch()
		return self.data

		# 

				



		

	

	#def display(data):
		