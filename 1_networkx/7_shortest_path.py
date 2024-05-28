import networkx as nx
import matplotlib.pyplot as plt

#create a edge list
edge_list = [(1,2),(2,3),(3,4),(3,5),(4,6),(6,7),(2,8),(8,9),(9,4)]

#create graph from this list
G = nx.Graph()
G.add_edges_from(edge_list)

#find the shortest path 
path = nx.shortest_path(G,2,4)
print("path:", path)

#spring
nx.draw_spectral(G,with_labels = True)
plt.show()