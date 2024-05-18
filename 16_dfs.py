# Reference https://www.programiz.com/dsa/graph-dfs
import networkx as nx 
import matplotlib.pyplot as plt
import random
import string
random.seed(9090)

def create_random_directed_graph(num_nodes):
    # Create a directed graph
    G = nx.DiGraph()
    
    # Add nodes
    nodes = list(string.ascii_uppercase[:num_nodes])
    G.add_nodes_from(nodes)
    
    # Add random edges
    for i in nodes:
        for j in nodes:
            if i != j:  # avoid self-loops for now
                if random.random() < 0.3:  # probability of 30% to create an edge
                    G.add_edge(i, j)
                    
    return G

# Number of nodes
num_nodes = 10

# Create a random directed graph with the specified number of nodes
random_digraph = create_random_directed_graph(num_nodes)
edges = random_digraph.edges()
print("edges:", edges)

def depth_first_search(start: str, edges: list):
    visited = []
    stack = [start]  

    while stack:
        node_to_visit = stack.pop(0)

        if node_to_visit not in visited:
            visited.append(node_to_visit)
            node_to_stack = []
            for u,v in edges:
                if u == node_to_visit and v not in visited:
                    node_to_stack.append(v)
                    if v in stack:
                        stack.remove(v)
            stack = sorted(node_to_stack) + stack

    return visited

start = "C"
print("start:", start)
visited = depth_first_search(start=start, edges=edges)
print("Visited:", visited)

G = nx.DiGraph()
G.add_edges_from(edges)

nx.draw_circular(G, with_labels = True)
plt.show()