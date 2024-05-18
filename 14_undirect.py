import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G_directed = nx.DiGraph()

# Add edges (and nodes)
G_directed.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4)])

# Draw the graph
plt.figure(figsize=(8, 6))
nx.draw(G_directed, with_labels=True, node_color='lightgreen', node_size=1500, edge_color='gray', arrows=True)
plt.title('Directed Graph')
plt.show()
