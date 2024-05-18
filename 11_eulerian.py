import networkx as nx
import matplotlib.pyplot as plt

# eulerian path: find a way to visit all edge ones
G1 = nx.complete_graph(5)
G2 = nx.complete_graph(5)
G2 = nx.relabel_nodes(G2, {0:"A", 1:"B", 2:"C", 3:"D", 4:"E"})

#create connection between G1 and G2
G_connector = nx.from_edgelist([(4,"X"), ("X", "A")])

G = nx.compose_all([G2,G1,G_connector])

eulerian_path = list( nx.eulerian_path(G))
print("eulerian_path:", eulerian_path)

#spring
nx.draw_spring(G,with_labels = True)
plt.show()


#example that graph has no eulerian path
edge_list = [(1,2),(2,3),(3,4),(3,5),(4,6),(6,7),(2,8),(8,9),(9,4)]

#create graph from this list
G = nx.Graph()
G.add_edges_from(edge_list)

eulerian_path = list( nx.eulerian_path(G))
print("eulerian_path:", eulerian_path)

#spring
nx.draw_spring(G,with_labels = True)
plt.show()
