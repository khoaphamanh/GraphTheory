import networkx as nx
import matplotlib.pyplot as plt

# Define the graph with weighted edges
edges = [
    ("A", "B", 2), ("B", "C", 3), ("C", "A", 1),
    ("C", "D", 4), ("D", "E", 2), ("E", "C", 1),
    ("F", "F", 1),
    ("G", "H", 3), ("H", "I", 2)
]

def plot_graph_with_weights(edges):
    G = nx.Graph()
    
    # Add edges along with weights
    for u, v, weight in edges:
        G.add_edge(u, v, weight=weight)

    pos = nx.circular_layout(G)  # Position nodes using the spring layout

    # Draw the graph
    nx.draw(G, pos, with_labels=True)
    
    # Draw edge labels
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    plt.title("Graph with Weights on Edges")
    plt.show()

plot_graph_with_weights(edges)
