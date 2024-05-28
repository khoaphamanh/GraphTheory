import networkx as nx
import matplotlib.pyplot as plt


#create complette graph, every node connect to each other
edge_list = [(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]

G = nx.Graph()
G.add_edges_from(edge_list)

#spring
nx.draw_spring(G,with_labels = True)
plt.show()

# another way to do that
G = nx.complete_graph(100)

#spring
nx.draw_spring(G,with_labels = True)
plt.show()