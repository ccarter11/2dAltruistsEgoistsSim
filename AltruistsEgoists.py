
from graphClass import graph
from nodeClass import node
import random
import matplotlib.pyplot as plt
import numpy as np
from pyvis.network import Network

class AESim:#2D altruist/egoist simulation 

	def __init__(self, numNodes, probAltruist, altruismCost, visualize):
		
		
		nodes = []
		simGraph = graph(nodes) # innitialize empty graph object
		label = 0
		rng = probAltruist*100 # set range based on input probability 
		
		for i in range(numNodes): # create nodes 
			label+= 1 
			nType = random.randint(1,100) - rng #change the chaces of setting agent to altruist based on user input prob
			if nType <= 0:
				nType = 'A'
				
				
			else:
				nType = 'E'
			
			simGraph.add_node(label,nType)
		simGraph.connectNodes() 
		

		
		self.data=[] #tracks number of altruists at each epoch 
		# self.data2 = [] #stores data from multiple sims
		self.simGraph = simGraph
		self.cost = -altruismCost 
		self.vis = visualize

		#create network visualization 
		if visualize==True: 
			net = Network(height='750px', width='100%', bgcolor='#222222', font_color='white')
			net.barnes_hut()
			labels = []
			for i,node in enumerate(self.simGraph.nodes): 
				if node.getType() == 'A':
					clr = '#3da831'
				else: 
					clr = '#3155a8'
				label = str(i+1) +':' + node.getType() 
				labels.append(label)
				net.add_node(label, color = clr,title = str(node.getLabel()))
			
			for node in self.simGraph.nodes: 
				for neighbor in node.edges:
					
					net.add_edge(labels[node.getLabel()-1],labels[neighbor.getLabel()-1])
			neighbor_map = net.get_adj_list()

# add neighbor data to node hover data
			for nd in net.nodes:
				nd['title'] += ' Neighbors:<br>' + '<br>'.join(neighbor_map[nd['id']])
				nd['value'] = len(neighbor_map[nd['id']])
			#net.repulsion(200, 10)
			net.show('network.html')
		
		
				

				

		
	

	def returnNumAlt(self):#sum the number of altruists currently in simGraph 
		numAlts = 0 
		for node in self.simGraph.nodes:
			if node.getType()=='A':
				numAlts+=1
		self.data.append(numAlts)
	
	

	def calcPayoff(self):
		#for each node in the simGraph, check the type of each neighbor and increment payoff accordingly
		for node in self.simGraph.nodes:
			if node.getType()== 'A':
				node.updatePayoff(self.cost)#start with cost of altruism for altruists
			for neighbor in node.edges: 
				if neighbor.getType()== 'A':
					node.updatePayoff(1)
			
			#print(node.getLabel(), node.getType(), node.getPayoff())

	def changeNodeType(self):
		#switch agent type if willChange == true 
		for node in self.simGraph.nodes:
			if node.getChange() == True:
				if node.getType()== 'A':
					node.updateType('E')
				elif node.getType()== 'E':
					node.updateType('A')
	def reset(self): 
		#reset agent attributes payoff and willChange to prepare for next epoch 
		for node in self.simGraph.nodes:
			node.updatePayoff((-node.getPayoff())) 
			node.updateChange(False)

	def calcEpoch(self,epochNum):#uses calcPayoff to determine if nodes will change type 
		altruists =[] 
		self.reset()
		self.calcPayoff() #initialize this epoch's node payoffs

		
		for node in self.simGraph.nodes: 
			#track the payoff of the respective types neighboring each node 
			altruistPayoff= 0  
			egoistPayoff = 0
			#number of neighboring altruists and egoists
			numAlt = 0 
			numEgo = 0
		
			#initialize based on current node type
			if node.getType()== 'A': 
				altruists.append(node.getLabel())
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
			#print(node.getLabel(), node.getType(),'ALT', avgAltPO, 'EGO', avgEgoPO)


			if ((avgAltPO>avgEgoPO) and node.getType() == 'E') or ((avgAltPO<avgEgoPO) and node.getType()=='A') :
				node.updateChange(True) 
		
			
			#print(node.getLabel(), node.getChange())
		if altruists != []:
			print('\n Altruists at epoch',epochNum,':', altruists)

		self.returnNumAlt()	
		

		#change all nodes' type accordingly for next epoch 
		self.changeNodeType() 

	


	def  runSim(self,  epochs, gen_graph):# run multiple epochs on the same graph, track the number of altruists 
		print('\n Adjacencies: ')
		for node in self.simGraph.nodes:
			edges=[]
			for neighbor in node.edges:
				edges.append(neighbor.getLabel())
			print(node.getLabel(),': ',edges)
			
		#Calls calc epoch 
		for i in range(epochs): 
			self.calcEpoch(i+1)
		result = self.data
		
		#create data visualization 
		if gen_graph == True:
			x = [0] * len(result)
			y = [0] * len(result)

			for i in range(0, len(result)):
				x[i] = i
				y[i] = result[i]

			
			# make the data
			np.random.seed(5)
			
	
			
			# plot
			fig, ax = plt.subplots()

			ax.scatter(x, y)

			ax.set(xlim=(0, len(result)), xticks=np.arange(0, len(result)+1),
				ylim=(0,max(result) ), yticks=np.arange(0, max(result)+10)
			)#result[1]

			yScale= 25
			ax.set_xticks(x[::2])
			#ax.set_yticks(y[::2])
			
			
			ax.set_xlabel('Epochs')
			ax.set_ylabel('Number of Altruists')
			
			plt.plot(x,y)
			plt.locator_params(axis='y', nbins=yScale)
			plt.show()
			
		else: 
			print('\nResult:',result)
			return result


			





	

		# 

				



		

	
