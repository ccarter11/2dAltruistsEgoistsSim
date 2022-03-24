
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
		label = 0
		endRange = 1/probAltruist
		for i in range(numNodes):
			label+= 1 
			#change based on user input probability
			nType = random.randint(0,endRange)
			if nType == 0:
				nType = 'A'
			else:
				nType = 'E'
			
			simGraph.add_node(label,nType)
		simGraph.connectNodes()
		#self.getnodes = simGraph.nodes
		
		#set random number of edges (and random conections) s.t. numNodes <|E| < numNodes**2
		# 
		#to check edges are added properly  
		for node in simGraph.nodes:
			gEdges =[]
			for neighbor in node.edges:
				gEdges.append(neighbor.getLabel())
			#print(gEdges)
				
					
			#self.getEdges = isEdges
		self.simGraph = simGraph
		self.cost = -altruismCost
		self.data=[]
		# for node in self.simGraph.nodes:
		# 	print(node.willChange())
		# print(len(self.simGraph.nodes))
				

				

		
	#def printNodesEdges():

	def returnNumAlt(self):
		numAlts = 0 
		for node in self.simGraph.nodes:
			if node.getType()=='A':
				numAlts+=1
		self.data.append(numAlts)
	
	

	def calcPayoff(self):
		#for each node in the simGraph, check the type of each neighbor and increment payoff accordingly
		for node in self.simGraph.nodes:
			if node.getType()== 'A':
				node.updatePayoff(self.cost)
			for neighbor in node.edges: 
				if neighbor.getType()== 'A':
					node.updatePayoff(1)
			
			print(node.getLabel(), node.getType(), node.getPayoff())

	def changeNodeType(self):
		for node in self.simGraph.nodes:
			if node.getChange() == True:
				if node.getType()== 'A':
					node.updateType('E')
				elif node.getType()== 'E':
					node.updateType('A')
	def reset(self):
		for node in self.simGraph.nodes:
			node.updatePayoff((-node.getPayoff())) 
			node.updateChange(False)

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


	def  runSim(self,  epochs):
		#Calls calc epoch 
		for i in range(epochs): 
			self.calcEpoch()
		print(self.data)
		return self.data

		# 

				



		

	

	#def display(data):
		