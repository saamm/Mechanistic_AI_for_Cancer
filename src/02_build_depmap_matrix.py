import pandas as pd

EXPR_FILE = "data/raw/depmap/OmicsExpressionTPMLogp1HumanProteinCodingGenes.csv"
MODEL_FILE = "data/raw/depmap/Model.csv"

OUT_EXPR = "data/processed/depmap/depmap_expression.csv"
OUT_META = "data/processed/depmap/depmap_metadata.csv"

# =========================
# LOAD EXPRESSION
# =========================

expr = pd.read_csv(EXPR_FILE)

print("Original shape:", expr.shape)

# =========================
# KEEP DEFAULT ENTRIES
# =========================

if "is_default_entry" in expr.columns:
    expr = expr[expr["is_default_entry"] == True]

# =========================
# SET INDEX
# =========================

expr = expr.set_index("ModelID")

# =========================
# REMOVE METADATA COLUMNS
# =========================

meta_cols = [
    "ProfileID",
    "is_default_entry",
    "SequencingID",
    "ModelConditionID",
    "IsDefaultEntryForMC",
    "IsDefaultEntryForModel"
]

existing = [c for c in meta_cols if c in expr.columns]

expr = expr.drop(columns=existing)

# =========================
# CLEAN GENE NAMES
# =========================

clean_cols = []

for col in expr.columns:

    # Example:
    # TP53 (7157) -> TP53

    gene = col.split(" (")[0]

    clean_cols.append(gene)

expr.columns = clean_cols

print("Cleaned shape:", expr.shape)

print("\nExample genes:")
print(expr.columns[:20])

# =========================
# SAVE EXPRESSION
# =========================

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

print("\nDone")