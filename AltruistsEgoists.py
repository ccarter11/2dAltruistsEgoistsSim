from graphClass import graph
from nodeClass import node
import random

class altruistEgoistSim2D:
#…atributes… 
	def __init__(self, numNodes, probAltruist):
		#self.nodes = numNodes 
		#self.pAlt= probAltruist
		nodes = []
		simGraph = graph(nodes)
		for i in range(numNodes):
			nType = random.randint(0,1)
			if nType == 0:
				nType = 'A'
			else:
				nType = 'E'
			simGraph.add_node(nType)
			simGraph.connectNodes(simGraph)
			self.getnodes = simGraph.nodes
			isEdges =[]
			for node in simGraph.nodes:
				if len(node.edges)>0:
					isEdges.append(True)
			self.getEdges = isEdges

				

			#simGraph = self.connectNodes(simGraph)
		

	#def printNodesEdges():


	#def  runSim(self,  epochs):
		#Calls calc epoch 
		# 
	#def calcEpoch(Graph, epoch, node data?):
		#calls calc epoch at each time


	#def calcPayoff(Graph, node data?):

	#def display(data):
		