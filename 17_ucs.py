# Reference https://www.educative.io/answers/what-is-uniform-cost-search
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
                if random.random() < 0.15:  # probability of 30% to create an edge
                    weight = random.randint(1, 10)  # Random weight between 1 and 10
                    G.add_edge(i, j, weight=weight)
                    
    return G

# Number of nodes
num_nodes = 10

# Create a random directed graph with the specified number of nodes
random_digraph = create_random_directed_graph(num_nodes)
edge_labels = nx.get_edge_attributes(random_digraph, 'weight')
print("edge_labels:", edge_labels)

def uniform_cost_search (start:str,edges_labels:dict):
    visited = {}
    frontier = {start:0}
    
    while frontier.keys():
        
        cost_node_to_visited = min(frontier.values())
        path_to_visited = next(path_node for (path_node,c) in frontier.items() if frontier[path_node] == cost_node_to_visited)

        
        node_to_visited = path_to_visited[-1]
        visited_nodes = [i[-1] for i in visited.keys()]

        frontier.pop(path_to_visited)
        if node_to_visited not in visited_nodes:
            
            visited[path_to_visited] = cost_node_to_visited
            
            new_path_dict = {}
            for (u,v), c in edges_labels.items():
                if u == node_to_visited and v != visited_nodes:
                    new_path_dict[(path_to_visited+v)] = cost_node_to_visited + c
            
            for u,v in new_path_dict.items():
                frontier[u] = v

    return visited

start = "B"
end = "F"
print("start:", start)
visited = uniform_cost_search(start=start,edges_labels=edge_labels)
print("visited:", visited)
shortes_path = [(i,j) for i,j in visited.items() if start in i and end in i]
print("shortes_path from {} to {}: {} cost {}".format(start,end,shortes_path[0][0],shortes_path[0][1]))

#check it with networkx
path = nx.shortest_path(random_digraph,start,end,weight="weight")
print("check with networkx")
print("path:", path)

# Draw the graph
pos = nx.circular_layout(random_digraph)
nx.draw(random_digraph, pos, with_labels=True)

# Draw edge labels
nx.draw_networkx_edge_labels(random_digraph, pos, edge_labels=edge_labels)
plt.show()