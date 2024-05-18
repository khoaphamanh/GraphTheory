import networkx as nx
import matplotlib.pyplot as plt

# eulerian path: find a way to visit all edge ones
G1 = nx.complete_graph(5)
G2 = nx.complete_graph(5)
G2 = nx.relabel_nodes(G2, {0:"A", 1:"B", 2:"C", 3:"D", 4:"E"})

#create connection between G1 and G2
G_connector = nx.from_edgelist([(4,"X")])
G = nx.compose_all([G2,G1,G_connector])

# connected components, return the group of nodes, that can go/ connected to each other
connected_component = list ( nx.connected_components(G))
print("connected_component:", connected_component)

#spring
nx.draw_shell(G,with_labels = True)
plt.show()