# Reference https://www.youtube.com/watch?v=DhtSZhakyOo
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
                    # Random weight between 1 and 10
                    weight = random.randint(1, 10)
                    G.add_edge(i, j, weight=weight)

    return G


# Number of nodes
num_nodes = 10

# Create a random directed graph with the specified number of nodes
random_digraph = create_random_directed_graph(num_nodes)
edge_labels = nx.get_edge_attributes(random_digraph, "weight")
print("edge_labels:", edge_labels)


# create heuristic cost
def create_heuristic_costs(num_nodes, start, goal):
    nodes = list(string.ascii_uppercase[:num_nodes])
    heuristic_costs = {}
    max_cost = 10
    min_cost = 0

    for n in nodes:
        c = random.randint(min_cost, max_cost)
        heuristic_costs[n] = c

    heuristic_costs[nodes[nodes.index(start)]] = max_cost
    heuristic_costs[nodes[nodes.index(goal)]] = min_cost

    return heuristic_costs


def a_star_search(start: str, edge_labels: dict, heuristic_costs: dict):
    visited = {}
    frontier = {start: 0}

    while frontier:

        cost_node_to_visited = min(frontier.values())
        path_to_visited = path_to_visited = next(
            path_node
            for (path_node, c) in frontier.items()
            if frontier[path_node] == cost_node_to_visited
        )

        node_to_visited = path_to_visited[-1]
        visited_nodes = [i[-1] for i in visited.keys()]
        frontier.pop(path_to_visited)

        if node_to_visited not in visited_nodes:

            visited[path_to_visited] = cost_node_to_visited

            new_path_dict = {}
            for (u, v), c in edge_labels.items():
                if u == node_to_visited and v != visited_nodes:
                    if len(path_to_visited) > 1:

                        node_heuristic_old = path_to_visited[-1]
                        cost_heuristic_old = heuristic_costs[node_heuristic_old]
                        cost_node_to_visited_without_last_node = (
                            cost_node_to_visited - cost_heuristic_old
                        )

                        cost_heuristic_new = heuristic_costs[v]
                        new_path_dict[(path_to_visited + v)] = (
                            cost_node_to_visited_without_last_node
                            + c
                            + cost_heuristic_new
                        )

                    else:
                        cost_heuristic_new = heuristic_costs[v]
                        new_path_dict[(path_to_visited + v)] = (
                            cost_node_to_visited + c + heuristic_costs[v]
                        )

            for u, v in new_path_dict.items():
                frontier[u] = v

    return visited


# start and goal node
start = "A"
goal = "J"
print("start_node:", start)
heuristic_costs = create_heuristic_costs(num_nodes=num_nodes, start=start, goal=goal)
print("heuristic_costs:", heuristic_costs)

visited = a_star_search(
    start=start, edge_labels=edge_labels, heuristic_costs=heuristic_costs
)
print("visited:", visited)

shortes_path = [(i, j) for i, j in visited.items() if start in i and goal in i]
print(
    "shortes_path from {} to {}: {} cost {}".format(
        start, goal, shortes_path[0][0], shortes_path[0][1]
    )
)

# Draw the graph
pos = nx.circular_layout(random_digraph)
nx.draw(random_digraph, pos, with_labels=True)

# Draw edge labels
nx.draw_networkx_edge_labels(random_digraph, pos, edge_labels=edge_labels)
plt.show()
