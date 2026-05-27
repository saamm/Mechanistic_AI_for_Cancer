import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# LOAD
X = pd.read_csv(
    "data/processed/pathways/tcga_kegg_ssgsea.csv",
    index_col=0
)

clusters = pd.read_csv(
    "data/processed/pathways/tcga_clusters.csv"
)

y = clusters["Cluster"]

# SPLIT
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# MODEL
model = RandomForestClassifier(
    n_estimators=500,
    random_state=42
)

model.fit(
    X_train,
    y_train
)

# EVALUATE
preds = model.predict(X_test)

print(
    classification_report(
        y_test,
        preds
    )
)

# FEATURE IMPORTANCE
importance = pd.DataFrame({
    "Pathway": X.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    "Importance",
    ascending=False
)

print("\nTop pathways:")
print(importance.head(20))

importance.to_csv(
    "results/pathway_importance.csv",
    index=False
)

print("\nSaved pathway importance.")