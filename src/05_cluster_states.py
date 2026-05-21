import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

import matplotlib.pyplot as plt

# ============================================
# CONFIG
# ============================================

INPUT = "data/processed/pathways/tcga_kegg_ssgsea.csv"

OUTPUT_CLUSTERS = "data/processed/pathways/tcga_clusters.csv"
OUTPUT_PCA = "data/processed/embeddings/tcga_pca_embeddings.csv"

FIGURE_PATH = "results/figures/tcga_tumor_states.png"

N_CLUSTERS = 3

# ============================================
# LOAD PATHWAY MATRIX
# ============================================

X = pd.read_csv(INPUT, index_col=0)

print("=" * 50)
print("TCGA PATHWAY MATRIX")
print("=" * 50)

print("\nShape:")
print(X.shape)

print("\nPreview:")
print(X.iloc[:5, :5])

# ============================================
# STANDARDIZE
# ============================================

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

print("\nData standardized.")

# ============================================
# PCA FOR VISUALIZATION
# ============================================

pca = PCA(n_components=10, random_state=42)

X_pca = pca.fit_transform(X_scaled)

explained = pca.explained_variance_ratio_

print("\nExplained variance ratio:")
print(explained[:10])

print("\nTotal explained variance:")
print(np.sum(explained))

# ============================================
# KMEANS CLUSTERING
# ============================================

kmeans = KMeans(
    n_clusters=N_CLUSTERS,
    random_state=42,
    n_init=50
)

clusters = kmeans.fit_predict(X_scaled)

# ============================================
# CLUSTER QUALITY
# ============================================

silhouette = silhouette_score(X_scaled, clusters)

print("\nSilhouette Score:")
print(silhouette)

# ============================================
# SAVE CLUSTER RESULTS
# ============================================

cluster_df = pd.DataFrame({
    "Sample": X.index,
    "Cluster": clusters,
    "PC1": X_pca[:, 0],
    "PC2": X_pca[:, 1],
    "PC3": X_pca[:, 2]
})

cluster_df.to_csv(
    OUTPUT_CLUSTERS,
    index=False
)

print(f"\nSaved cluster assignments:")
print(OUTPUT_CLUSTERS)

# ============================================
# SAVE PCA EMBEDDINGS
# ============================================

embedding_cols = [
    f"PC{i+1}" for i in range(X_pca.shape[1])
]

embedding_df = pd.DataFrame(
    X_pca,
    index=X.index,
    columns=embedding_cols
)

embedding_df.to_csv(
    OUTPUT_PCA
)

print(f"\nSaved PCA embeddings:")
print(OUTPUT_PCA)

# ============================================
# VISUALIZATION
# ============================================

plt.figure(figsize=(10, 8))

scatter = plt.scatter(
    X_pca[:, 0],
    X_pca[:, 1],
    c=clusters,
    s=60,
    alpha=0.8
)

plt.xlabel("PC1", fontsize=12)
plt.ylabel("PC2", fontsize=12)

plt.title(
    "TCGA Tumor States from KEGG Pathway Activity",
    fontsize=14
)

plt.grid(alpha=0.2)

plt.savefig(
    FIGURE_PATH,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print(f"\nSaved figure:")
print(FIGURE_PATH)

# ============================================
# CLUSTER DISTRIBUTION
# ============================================

print("\nCluster Distribution:")
print(cluster_df["Cluster"].value_counts())

print("\nDone.")