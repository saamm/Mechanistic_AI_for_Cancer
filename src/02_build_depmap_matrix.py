import pandas as pd

EXPR_FILE = "data/raw/depmap/OmicsExpressionTPMLogp1HumanProteinCodingGenes.csv"
MODEL_FILE = "data/raw/depmap/Model.csv"

OUT_EXPR = "data/processed/depmap/depmap_expression.csv"
OUT_META = "data/processed/depmap/depmap_metadata.csv"

# =========================
# LOAD EXPRESSION
# =========================

expr = pd.read_csv(EXPR_FILE)

print(expr.shape)

# Keep default entries only if available
if "is_default_entry" in expr.columns:
    expr = expr[expr["is_default_entry"] == True]

# Set index
expr = expr.set_index("ModelID")

# Remove metadata columns
meta_cols = [
    "ProfileID",
    "is_default_entry"
]

existing = [c for c in meta_cols if c in expr.columns]

expr = expr.drop(columns=existing)

print(expr.shape)

expr.to_csv(OUT_EXPR)

# =========================
# LOAD MODEL METADATA
# =========================

meta = pd.read_csv(MODEL_FILE)

keep_cols = [
    "ModelID",
    "CellLineName",
    "OncotreeLineage",
    "OncotreePrimaryDisease",
    "OncotreeSubtype"
]

meta = meta[keep_cols]

meta.to_csv(OUT_META, index=False)

print("Done")