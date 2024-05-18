import networkx as nx
import matplotlib.pyplot as plt

#create a edge list
edge_list = [(1,2),(2,3),(3,4),(3,5),(4,6),(6,7)]

#create graph from this list
G = nx.Graph()
G.add_edges_from(edge_list)

#spring
nx.draw_spring(G,with_labels = True)
plt.show()

#circular try to plot nodes in circle way
nx.draw_circular(G,with_labels = True)
plt.show()

#shell try to plot nodes in circle way ( conzentris circle (đồng tâm))
nx.draw_shell(G,with_labels = True)
plt.show()

#spectral same as spring???
nx.draw_spectral(G,with_labels = True)
plt.show()

#random plot nodes randomly
nx.draw_random(G,with_labels = True)
plt.show()

#planar edges dont cut each other 
nx.draw_planar(G,with_labels = True)
plt.show()