import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add nodes
nodes = ["Alice", "Bob", "Charlie"]
G.add_nodes_from(nodes)

# Add edges
edges = [("Alice", "Bob"), ("Bob", "Charlie"), ("Charlie", "Alice")]
G.add_edges_from(edges)

# Draw the graph
pos = nx.spring_layout(G, seed=42)

fig, ax = plt.subplots(figsize=(8, 6))

nx.draw_networkx_nodes(G, pos, ax=ax, node_color='red', node_size=2000)

nx.draw_networkx_edges(G, pos, ax=ax, edge_color='black')

nx.draw_networkx_labels(G, pos, ax=ax, font_size=16, font_weight='bold')

plt.title("Directed Graph")
plt.show()