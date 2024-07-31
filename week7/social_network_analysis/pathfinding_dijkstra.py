import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Define the cities and roads with distances
edges = [
    ("A", "B", 10),
    ("A", "C", 15),
    ("B", "C", 12),
    ("B", "D", 15),
    ("C", "D", 10),
    ("C", "E", 5),
    ("D", "E", 8),
    ("D", "F", 20),
    ("E", "F", 10),
    ("A", "G", 25),
    ("B", "H", 18),
    ("D", "J", 12),
    ("E", "K", 15),
    ("F", "L", 30),
    ("G", "H", 22),
    ("H", "I", 17),
    ("I", "J", 14),
    ("J", "K", 19),
    ("K", "L", 13),
    ("L", "G", 28),
    ("H", "J", 16),
    ("I", "L", 21)
]

# Add edges with weights to the graph
G.add_weighted_edges_from(edges)

# Use Dijkstra's algorithm to find the shortest path from A to F
shortest_path = nx.shortest_path(G, source="A", target="K")
shortest_path_length = nx.shortest_path_length(G, source="A", target="K")

# Print the shortest path and its length
print(f"Shortest path from A to F: {shortest_path}")
print(f"Length of the shortest path: {shortest_path_length} km")

# Draw the graph
pos = nx.spring_layout(G, seed=42)
fig, ax = plt.subplots(figsize=(12, 10))

# Draw nodes
nx.draw_networkx_nodes(G, pos, ax=ax, node_color='lightblue', node_size=2000, alpha=0.7)

# Draw edges
nx.draw_networkx_edges(G, pos, ax=ax, edge_color='gray', width=1.5)

# Highlight shortest path edges
path_edges = list(zip(shortest_path, shortest_path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)

# Draw labels
nx.draw_networkx_labels(G, pos, ax=ax, font_size=12, font_weight='bold')

# Draw edge labels with distances
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='black')

plt.title(f"Shortest Path from A to F\nLength: {shortest_path_length} km")
plt.show()


