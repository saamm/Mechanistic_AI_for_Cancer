import pandas as pd
import networkx as nx
from node2vec import Node2Vec

# LOAD NETWORK

GRAPH_PATH = "results/networks/cluster_2.graphml"

G = nx.read_graphml(GRAPH_PATH)

print("=" * 50)
print("GRAPH LOADED")
print("=" * 50)

print("Nodes:", G.number_of_nodes())
print("Edges:", G.number_of_edges())

# FIX NEGATIVE WEIGHTS

for u, v, d in G.edges(data=True):

    weight = float(d["weight"])

    # Node2Vec requires non-negative probabilities
    d["weight"] = abs(weight)

print("\nNegative weights fixed.")

# NODE2VEC EMBEDDINGS

node2vec = Node2Vec(
    G,
    dimensions=64,
    walk_length=20,
    num_walks=200,
    workers=1,   # safer on Windows
    seed=42,
    weight_key="weight"
)

print("\nTraining Node2Vec...")

model = node2vec.fit(
    window=10,
    min_count=1,
    batch_words=4
)

print("Training complete.")


# SAVE EMBEDDINGS
embeddings = []

for node in G.nodes():

    vector = model.wv[node]

    row = [node] + list(vector)

    embeddings.append(row)

cols = ["Pathway"] + [
    f"emb_{i}" for i in range(64)
]

df = pd.DataFrame(
    embeddings,
    columns=cols
)

OUTPUT = "results/graph_embeddings.csv"

df.to_csv(
    OUTPUT,
    index=False
)

print("\nSaved embeddings:")
print(OUTPUT)

print("\nDone.")