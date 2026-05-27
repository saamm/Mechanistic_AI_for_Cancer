import pandas as pd
import networkx as nx
import numpy as np
import os

# CREATE ABSOLUTE PATHS

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

DATA_DIR = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "pathways"
)

RESULTS_DIR = os.path.join(
    BASE_DIR,
    "results"
)

NETWORK_DIR = os.path.join(
    RESULTS_DIR,
    "networks"
)

# FORCE CREATE FOLDERS
os.makedirs(
    NETWORK_DIR,
    exist_ok=True
)

print("=" * 50)
print("DIRECTORY CHECK")
print("=" * 50)

print("\nBASE_DIR:")
print(BASE_DIR)

print("\nNETWORK_DIR:")
print(NETWORK_DIR)

print("\nFolder exists?")
print(os.path.exists(NETWORK_DIR))

# LOAD DATA

PATHWAY_FILE = os.path.join(
    DATA_DIR,
    "tcga_kegg_ssgsea.csv"
)

CLUSTER_FILE = os.path.join(
    DATA_DIR,
    "tcga_clusters.csv"
)

pathways = pd.read_csv(
    PATHWAY_FILE,
    index_col=0
)

clusters = pd.read_csv(
    CLUSTER_FILE
)

# MERGE CLUSTERS
pathways["cluster"] = clusters["Cluster"].values

# BUILD NETWORKS
THRESHOLD = 0.7

for cluster_id in sorted(pathways["cluster"].unique()):

    subset = pathways[
        pathways["cluster"] == cluster_id
    ]

    subset = subset.drop(
        columns=["cluster"]
    )

    # pathway-pathway correlations
    corr = subset.corr()

    G = nx.Graph()

    # BUILD EDGES

    for i in corr.columns:

        for j in corr.columns:

            if i >= j:
                continue

            value = corr.loc[i, j]

            if abs(value) > THRESHOLD:

                G.add_edge(
                    str(i),
                    str(j),
                    weight=float(value)
                )

    # OUTPUT STATS

    print(f"\nCluster {cluster_id}")
    print("Nodes:", G.number_of_nodes())
    print("Edges:", G.number_of_edges())

    # SAVE GRAPHML

    graphml_path = os.path.join(
        NETWORK_DIR,
        f"cluster_{cluster_id}.graphml"
    )

    nx.write_graphml(
        G,
        graphml_path
    )

    print("Saved:")
    print(graphml_path)

print("\nNetworks saved successfully.")