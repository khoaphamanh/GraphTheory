import networkx as nx
import matplotlib.pyplot as plt

# centrality nói về 1 node là trung tâm của đồ thị, node trung tâm của đồ thị là node có độ dài trung bình đường đi ngắn nhất qua các node khác là ngắn nhất
edge_list = [(1,2),(2,3),(3,4),(3,5),(4,6),(6,7),(2,8),(8,9),(9,4)]

#create graph from this list
G = nx.Graph()
G.add_edges_from(edge_list)

nodes = G.nodes
print("nodes:", nodes)

degree = dict(G.degree)
print("degree:", degree)

# degree centrality = degree / [nodes - 1]
degree_centrality = nx.degree_centrality(G)
print("degree_centrality:", degree_centrality)

# closeness centrality = 1 / sum (shortest path from this node to all other nodes)
closeness_centrality = nx.closeness_centrality(G)
print("closeness_centrality:", closeness_centrality)

eigenvector_centrality = nx.eigenvector_centrality(G)
print("eigenvector_centrality:", eigenvector_centrality)

# centrality
centrality = nx.betweenness_centrality(G)
print("centrality:", centrality)

#spring
nx.draw_spectral(G,with_labels = True)
plt.show()