import networkx as nx
import matplotlib.pyplot as plt

# create a undirected graph
G = nx.Graph()

#create edge between node 1 and 2, if node do not exist, create nodes
G.add_edge(1,2)

#weight means how strong the connection between nodes
G.add_edge(2,3,weight = 0.9)

G.add_edge("A", "B")
G.add_edge("B", "B")

# add new node
G.add_node("C")

# add new node as object ( function )
G.add_node(print)

#visualize
nx.draw_spring(G,with_labels = True)
plt.show()
