import networkx as nx
import matplotlib.pyplot as plt

# Create an undirected graph
G = nx.Graph()

# Define the students and their friendships
students = [
    "Aisha", "Carlos", "Mei", "Arun", "Billy", "Jamil",
    "Sofia", "Raj", "Priya", "Omar", "Emma", "Diego"
]

friendships = [
    ("Aisha", "Carlos"),
    ("Aisha", "Arun"),
    ("Carlos", "Mei"),
    ("Carlos", "Billy"),
    ("Mei", "Jamil"),
    ("Arun", "Billy"),
    ("Sofia", "Raj"),
    ("Raj", "Priya"),
    ("Priya", "Omar"),
    ("Emma", "Diego"),
    ("Diego", "Jamil")
]

# Add nodes and edges to the graph
G.add_nodes_from(students)
G.add_edges_from(friendships)

# Check if the graph is connected
is_connected = nx.is_connected(G)
print(f"The graph is {'connected' if is_connected else 'not connected'}.")

# Find and print clusters (connected components)
clusters = list(nx.connected_components(G))
print(f"The graph contains {len(clusters)} cluster(s):")
for i, cluster in enumerate(clusters, 1):
    print(f"Cluster {i}: {cluster}")


# Draw the graph
pos = nx.spring_layout(G, seed=42)
fig, ax = plt.subplots(figsize=(10, 8))

nx.draw_networkx_nodes(G, pos, ax=ax, node_color='lightblue', node_size=2000, alpha=0.3)
nx.draw_networkx_edges(G, pos, ax=ax, edge_color='gray')
nx.draw_networkx_labels(G, pos, ax=ax, font_size=16, font_weight='light')

plt.title("Friendship Network")
plt.show()

