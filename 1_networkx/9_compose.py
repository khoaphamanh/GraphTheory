import networkx as nx
import matplotlib.pyplot as plt


#create 2 complete graph
G1 = nx.complete_graph(5)
G2 = nx.complete_graph(5)
G2 = nx.relabel_nodes(G2, {0:"A", 1:"B", 2:"C", 3:"D", 4:"E"})

#create connection between G1 and G2
G_connector = nx.from_edgelist([(4,"X"), ("X", "A")])

G = nx.compose_all([G2,G1,G_connector])

degree_centrality = nx.degree_centrality(G)
print("degree_centrality:", degree_centrality)

centrality = nx.betweenness_centrality(G)
print("centrality:", centrality)

nodes = G.nodes
print("nodes len:", len(nodes))
print("nodes:", nodes)

edges = G.edges 
print("edges len:", len(edges))
print("edges:", edges)

# nodes / (possible edges) in this case is 11 / (22*2). 22*2 because of 2 direction between 2 nodes
density = nx.density(G)
print("density:", density)

#diameter = longest shortest path
diameter = nx.diameter(G)
print("diameter:", diameter)

#spring
nx.draw_spring(G,with_labels = True)
plt.show()