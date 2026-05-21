import pandas as pd

INPUT = "data/processed/tcga/tcga_tpm_matrix.csv"
OUTPUT = "data/processed/tcga/tcga_tpm_matrix_transposed.csv"


df = pd.read_csv(INPUT, index_col=0)

# transpose

df = df.T

print(df.shape)

# save

df.to_csv(OUTPUT)