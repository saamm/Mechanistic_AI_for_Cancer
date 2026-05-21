import os
import pandas as pd
from tqdm import tqdm

# ======================
# CONFIG
# ======================

TCGA_DIR = "data/raw/tcga"
OUTPUT_FILE = "data/processed/tcga/tcga_tpm_matrix.csv"

# ======================
# LOAD FILES
# ======================

all_samples = []

files = [f for f in os.listdir(TCGA_DIR) if f.endswith(".tsv")]

print(f"Found {len(files)} TCGA files")

for file in tqdm(files):

    path = os.path.join(TCGA_DIR, file)

    try:

        # IMPORTANT FIX
        df = pd.read_csv(path, sep="\t", comment="#")

        # Keep protein coding genes
        df = df[df["gene_type"] == "protein_coding"]

        # Remove duplicates
        df = df.drop_duplicates(subset="gene_name")

        sample_name = file.replace(".tsv", "")

        # TPM expression
        sample_expr = df[["gene_name", "tpm_unstranded"]].copy()

        sample_expr.columns = ["gene", sample_name]

        sample_expr = sample_expr.set_index("gene")

        all_samples.append(sample_expr)

    except Exception as e:
        print(f"Error processing {file}: {e}")

# ======================
# MERGE
# ======================

merged = pd.concat(all_samples, axis=1)

merged = merged.fillna(0)

print("\nFinal matrix shape:", merged.shape)

# ======================
# SAVE
# ======================

merged.to_csv(OUTPUT_FILE)

print(f"Saved to {OUTPUT_FILE}")