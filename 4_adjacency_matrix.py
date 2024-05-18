import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

#create a edge list
edge_list = [(1,2),(2,3),(3,4),(3,5),(4,6),(6,7)]

#create graph from this list
G = nx.Graph()
G.add_edges_from(edge_list)

#get the adjacency matrix: matrix that show which pair of nodes are connected by an edge
adjacency_matrix = nx.adjacency_matrix(G)
print("adjacency_matrix:", adjacency_matrix)

# create adjacency matrix from numpy ( for directed graph)
matrix = np.array([[0,1,0],
                   [1,1,1],
                   [0,0,0]])

G = nx.from_numpy_array(matrix)

#visualize
nx.draw_spring(G,with_labels = True)
plt.show()