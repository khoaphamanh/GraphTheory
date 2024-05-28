import networkx as nx
import matplotlib.pyplot as plt

#create a edge list
edge_list = [(1,2),(2,3),(3,4),(3,5),(4,6),(6,7)]

#create graph from this list
G = nx.from_edgelist(edgelist=edge_list)

#visualize
nx.draw_spring(G,with_labels = True)
plt.show()

#another way to do that
G = nx.Graph()
G.add_edges_from(edge_list)

#visualize
nx.draw_spring(G,with_labels = True)
plt.show()
