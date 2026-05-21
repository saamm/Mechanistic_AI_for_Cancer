import pandas as pd
from scipy.stats import ttest_ind
from statsmodels.stats.multitest import multipletests

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

# merge
df = pathways.copy()
df["cluster"] = clusters["Cluster"]

# =========================
# DIFFERENTIAL ANALYSIS
# =========================

results = []

pathway_cols = pathways.columns

for pathway in pathway_cols:

    for c1 in sorted(df["cluster"].unique()):

        for c2 in sorted(df["cluster"].unique()):

            if c1 >= c2:
                continue

            g1 = df[df["cluster"] == c1][pathway]
            g2 = df[df["cluster"] == c2][pathway]

            stat, pval = ttest_ind(g1, g2)

            effect = g1.mean() - g2.mean()

            results.append({
                "pathway": pathway,
                "cluster1": c1,
                "cluster2": c2,
                "pvalue": pval,
                "effect_size": effect
            })

# =========================
# SAVE
# =========================

res = pd.DataFrame(results)

res["adj_p"] = multipletests(
    res["pvalue"],
    method="fdr_bh"
)[1]

res = res.sort_values("adj_p")

print(res.head(20))

res.to_csv(
    "results/differential_pathways.csv",
    index=False
)

print("\nSaved differential pathways.")
