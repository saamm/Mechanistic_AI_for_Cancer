# Mechanistic_AI_for_Cancer

A systems biology and machine learning project exploring cancer-associated signaling networks using pathway-level representations, graph learning, and interpretable machine learning on large-scale omics data.

---

# Overview

This project investigates how pathway-level biological activity can be used to uncover heterogeneous tumor states and identify important signaling programs associated with cancer.

Instead of relying only on individual genes or proteins, the workflow transforms omics data into pathway activity representations and studies:

- pathway interactions
- signaling rewiring
- graph structure
- latent biological organization
- interpretable ML biomarkers

The project combines:

- pathway scoring
- network analysis
- graph representation learning
- clustering
- Random Forest classification
- feature importance analysis

to build a mechanistic view of cancer biology.

---

# Objectives

- Identify heterogeneous tumor states from pathway activity
- Construct pathway interaction networks
- Learn latent graph representations of signaling pathways
- Discover biologically meaningful pathway modules
- Train interpretable ML models for tumor state prediction
- Identify candidate signaling biomarkers

---

# Workflow

```text
Raw Omics Data
        ↓
Preprocessing & Scaling
        ↓
Pathway Activity Scoring
        ↓
Pathway Correlation Networks
        ↓
Graph Representation Learning
        ↓
Pathway Embeddings
        ↓
Clustering + ML Classification
        ↓
Biological Interpretation
```

---

# Methods

## 1. Data Preprocessing

- Missing value filtering
- Variance-based feature selection
- Scaling and normalization

## 2. Pathway-Level Representation

Biological pathways were used as higher-level functional units instead of analyzing isolated molecular features.

Examples include:

- MAPK signaling
- PI3K-Akt signaling
- JAK-STAT signaling
- Calcium signaling
- TNF signaling
- Cancer-associated pathways

## 3. Network Construction

Pathway interaction graphs were generated using correlation-based relationships between pathway activities.

The resulting networks were used to study:

- signaling connectivity
- pathway hubs
- biological modules
- network rewiring

## 4. Graph Representation Learning

Graph embeddings were learned to encode pathway network structure into low-dimensional vector representations.

This allowed the model to capture:

- pathway similarity
- shared signaling behavior
- latent biological organization

## 5. Machine Learning

A Random Forest classifier was trained on pathway-level features to predict tumor-related clusters.

---

# Results

## Classification Performance

```text
Accuracy: 98%

Precision / Recall / F1-score:

Cluster 0:
Precision = 1.00
Recall = 1.00
F1-score = 1.00

Cluster 1:
Precision = 0.95
Recall = 1.00
F1-score = 0.98

Cluster 2:
Precision = 1.00
Recall = 0.94
F1-score = 0.97
```

These results demonstrate that pathway-level features contain strong predictive biological signal.

---

# Important Pathways Identified

Top predictive pathways included:

| Pathway | Importance |
|---|---|
| Amoebiasis | 0.028 |
| Transcriptional misregulation in cancer | 0.026 |
| Yersinia infection | 0.024 |
| Epstein-Barr virus infection | 0.022 |
| Pathways in cancer | 0.021 |
| JAK-STAT signaling pathway | 0.017 |
| TNF signaling pathway | 0.017 |
| Ras signaling pathway | 0.017 |
| Calcium signaling pathway | 0.015 |
| Viral carcinogenesis | 0.015 |

Many identified pathways are strongly associated with:

- inflammation
- immune signaling
- carcinogenesis
- cellular proliferation
- tumor microenvironment dynamics

---

# Candidate Biomarkers

The project identified candidate biomarkers from highly important pathways and associated proteins.

These biomarkers may reflect:

- tumor signaling states
- immune activity
- metabolic rewiring
- cancer progression mechanisms

---

# Graph Representation Learning Insights

Graph embeddings revealed biologically meaningful pathway organization.

Distinct groups of pathways emerged, including:

## Cancer / Invasion Programs

- ECM-receptor interaction
- PI3K-Akt signaling
- MAPK signaling
- Focal adhesion
- Regulation of actin cytoskeleton

## Metabolic / Stress Response Programs

- AMPK signaling
- FoxO signaling
- Insulin signaling
- Longevity regulating pathway

## Immune / Inflammatory Programs

- Cytokine signaling
- Viral infection pathways
- Rheumatoid arthritis
- TNF signaling

These results suggest that graph representation learning can recover latent biological structure from pathway interaction networks.

---

# Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- NetworkX
- Matplotlib
- Seaborn
- Graph Representation Learning
- Pathway Enrichment Analysis

---

# Future Directions

- Apply Graph Neural Networks (GNNs)
- Integrate multi-omics datasets
- Use real protein-protein interaction priors
- Perform survival analysis
- Validate biomarkers experimentally
- Build explainable mechanistic AI systems for cancer biology

---

# Repository Structure

```text
Mechanistic_AI_for_Cancer/
│
├── data/
│   ├── raw/
│   ├── processed/
│
│
├── results/
│   ├── figures/
│   ├── networks/
│
├── src/
│
├── README.md
│
└── requirements.txt
```

---

# Key Takeaway

This project demonstrates how pathway-level systems biology combined with graph learning and interpretable machine learning can recover meaningful cancer signaling structure from large-scale biological data.

The workflow highlights the potential of mechanistic AI approaches for discovering biologically grounded tumor representations and candidate biomarkers.

---

# Author

Soumya Sinha

MSc Data Science  
Interested in:
- Machine Learning
- Computational Biology
- Systems Biology
- Mechanistic AI
- Biomedical AI
