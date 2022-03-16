import imp
from  AltruistsEgoists import altruistEgoistSim2D
from nodeClass import node
from graphClass import graph

test1 = altruistEgoistSim2D(20,.1,.25)

# print(test1.getnodes)
# print(test1.getEdges)
test1.runSim(2)
