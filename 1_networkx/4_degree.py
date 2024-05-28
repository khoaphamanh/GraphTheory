import networkx as nx
import matplotlib.pyplot as plt

#create complette graph, every node connect to each other
edge_list = [(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]

G = nx.Graph()
G.add_edges_from(edge_list)

#degree tells how many edge that are incident to this node
print(dict(G.degree))

#spring
nx.draw_spring(G,with_labels = True)
plt.show()

#create a edge list
edge_list = [(1,2),(2,3),(3,4),(3,5),(4,6),(6,7)]

#create graph from this list
G = nx.Graph()
G.add_edges_from(edge_list)

print(dict(G.degree))

#spring
nx.draw_spring(G,with_labels = True)
plt.show()




#out degree and in degree for directed graph
edge_list = [(1,2),(2,3),(3,4),(3,5),(4,6),(6,7)]
G = nx.DiGraph()
G.add_edges_from(edge_list)

out_degree = G.out_degree
print("out_degree:", out_degree)

in_degree = G.in_degree
print("in_degree:", in_degree)

#spring
nx.draw_spring(G,with_labels = True)
plt.show()