import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

interactions = [
    ("A", "B"),
    ("A", "C"),
    ("B", "D"),
    ("C", "E"),
    ("D", "F"),
    ("E", "A"),
    ("E", "B"),
    ("F", "C")
]

G.add_edges_from(interactions)


degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G, normalized=True)
closeness_centrality = nx.closeness_centrality(G)
eigenvector_centrality = nx.eigenvector_centrality(G)

print("Degree Centrality:", degree_centrality)
print("Betweenness Centrality:", betweenness_centrality)
print("Closeness Centrality:", closeness_centrality)
print("Eigenvector Centrality:", eigenvector_centrality)

pos = nx.spring_layout(G, seed=42)
fig, ax = plt.subplots(figsize=(10, 8))

nx.draw_networkx_nodes(G, pos, ax=ax, node_color='red', node_size=2000, alpha=0.3)
nx.draw_networkx_edges(G, pos, ax=ax, edge_color='blue')
nx.draw_networkx_labels(G, pos, ax=ax, font_size=16, font_weight='light')

plt.title("Twitter Interaction Network")
plt.show()

