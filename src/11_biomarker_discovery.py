import pandas as pd

# LOAD
importance = pd.read_csv(
    "results/pathway_importance.csv"
)

diff = pd.read_csv(
    "results/differential_pathways.csv"
)

# SIGNIFICANT PATHWAYS
sig = diff[
    diff["adj_p"] < 0.001
]
# MERGE
merged = pd.merge(
    sig,
    importance,
    left_on="pathway",
    right_on="Pathway"
)

merged = merged.sort_values(
    ["Importance", "adj_p"],
    ascending=[False, True]
)

# SAVE
merged.to_csv(
    "results/candidate_biomarkers.csv",
    index=False
)

print("\nTop candidate biomarkers:")
print(
    merged.head(20)
)

print("\nSaved biomarkers.")