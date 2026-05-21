import pandas as pd

TCGA = "data/processed/tcga/tcga_tpm_matrix_transposed.csv"
DEPMAP = "data/processed/depmap/depmap_expression.csv"

OUT_TCGA = "data/processed/shared/tcga_shared.csv"
OUT_DEPMAP = "data/processed/shared/depmap_shared.csv"

# ======================
# LOAD
# ======================


tcga = pd.read_csv(TCGA, index_col=0)
depmap = pd.read_csv(DEPMAP, index_col=0)

# ======================
# INTERSECT GENES
# ======================

shared_genes = list(set(tcga.columns) & set(depmap.columns))

print("Shared genes:", len(shared_genes))

# ======================
# SUBSET
# ======================

tcga = tcga[shared_genes]
depmap = depmap[shared_genes]

# ======================
# SAVE
# ======================

tcga.to_csv(OUT_TCGA)
depmap.to_csv(OUT_DEPMAP)

print("Saved shared matrices")