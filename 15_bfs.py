# Reference https://www.youtube.com/watch?v=oDqjPvD54Ss&t=118s
import networkx as nx 
import matplotlib.pyplot as plt

edges = [
    ("A", "B"), ("B", "C"), ("C", "A"),
    ("C", "D"), ("D", "E"), ("E", "C"),
    ("F", "F"),
    ("G", "H"), ("H", "I")
]

def breadth_first_search(start: str, edges: list):
    visited = []
    queue = [start]  # Initialize the queue with the start node

    while queue:
        node_to_visit = queue.pop(0)  # Dequeue the first node

        if node_to_visit not in visited:
            visited.append(node_to_visit)

            for u, v in edges:
                if u == node_to_visit and v not in visited and v not in queue:
                    queue.append(v)

    return visited

start = "A"
print("start:", start)
visited = breadth_first_search(start=start, edges=edges)
print("Visited:", visited)

G = nx.DiGraph()
G.add_edges_from(edges)

nx.draw_circular(G, with_labels = True)
plt.show()