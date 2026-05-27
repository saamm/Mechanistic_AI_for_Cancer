import pandas as pd
import networkx as nx
import numpy as np

# =========================
# LOAD
# =========================

pathways = pd.read_csv(
    "data/processed/pathways/tcga_kegg_ssgsea.csv",
    index_col=0
)

clusters = pd.read_csv(
    "data/processed/pathways/tcga_clusters.csv",
    index_col=0
)

pathways["cluster"] = clusters["Cluster"]

# =========================
# BUILD NETWORKS
# =========================

for cluster_id in sorted(pathways["cluster"].unique()):

    subset = pathways[pathways["cluster"] == cluster_id]

    subset = subset.drop(columns=["cluster"])

    corr = subset.corr()

    G = nx.Graph()

    threshold = 0.7

    for i in corr.columns:
        for j in corr.columns:

            if i == j:
                continue

            value = corr.loc[i, j]

            if abs(value) > threshold:

                G.add_edge(
                    i,
                    j,
                    weight=value
                )

    print(f"\nCluster {cluster_id}")
    print("Nodes:", G.number_of_nodes())
    print("Edges:", G.number_of_edges())

    nx.write_gml(
        G,
        f"results/networks/cluster_{cluster_id}.gml"
    )

print("\nNetworks saved.")