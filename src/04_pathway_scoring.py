import pandas as pd
import gseapy as gp

# =========================
# CONFIG
# =========================

INPUT = "data/processed/shared/tcga_shared.csv"
OUTPUT = "data/processed/pathways/tcga_kegg_ssgsea.csv"

# =========================
# LOAD DATA
# =========================

expr = pd.read_csv(INPUT, index_col=0)

print("Original shape:", expr.shape)

# Current:
# samples × genes

# ssGSEA expects:
# genes × samples

expr = expr.T

print("Transposed shape:", expr.shape)

# =========================
# RUN ssGSEA
# =========================

results = gp.ssgsea(
    data=expr,
    gene_sets="KEGG_2021_Human",
    sample_norm_method='rank',
    outdir=None,
    no_plot=True,
    processes=4,
    min_size=5,
    max_size=1000
)

# =========================
# EXTRACT SCORES
# =========================

scores = results.res2d

print(scores.head())

# =========================
# CONVERT TO MATRIX
# =========================

pathway_matrix = scores.pivot(
    index="Name",
    columns="Term",
    values="NES"
)

print("\nPathway matrix shape:")
print(pathway_matrix.shape)

print("\nPreview:")
print(pathway_matrix.iloc[:5, :5])

# =========================
# SAVE
# =========================

pathway_matrix.to_csv(OUTPUT)

print(f"\nSaved to: {OUTPUT}")