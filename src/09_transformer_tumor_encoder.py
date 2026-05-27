import pandas as pd
import torch
import torch.nn as nn
from sklearn.preprocessing import StandardScaler
from torch.utils.data import Dataset, DataLoader

# LOAD
df = pd.read_csv(
    "data/processed/pathways/tcga_kegg_ssgsea.csv",
    index_col=0
)

X = df.values

# SCALE
scaler = StandardScaler()

X = scaler.fit_transform(X)

X = torch.tensor(
    X,
    dtype=torch.float32
)

# DATASET
class TumorDataset(Dataset):

    def __init__(self, X):
        self.X = X

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        return self.X[idx]

dataset = TumorDataset(X)

loader = DataLoader(
    dataset,
    batch_size=16,
    shuffle=True
)

# TRANSFORMER
class TumorTransformer(nn.Module):

    def __init__(self):

        super().__init__()

        self.embedding = nn.Linear(
            320,
            128
        )

        encoder_layer = nn.TransformerEncoderLayer(
            d_model=128,
            nhead=8,
            batch_first=True
        )

        self.transformer = nn.TransformerEncoder(
            encoder_layer,
            num_layers=3
        )

        self.decoder = nn.Linear(
            128,
            320
        )

    def forward(self, x):

        x = self.embedding(x)

        x = x.unsqueeze(1)

        x = self.transformer(x)

        x = x.squeeze(1)

        x = self.decoder(x)

        return x

model = TumorTransformer()

# TRAINING
optimizer = torch.optim.Adam(
    model.parameters(),
    lr=1e-3
)

criterion = nn.MSELoss()

# TRAIN
for epoch in range(50):

    total_loss = 0

    for batch in loader:

        optimizer.zero_grad()

        output = model(batch)

        loss = criterion(output, batch)

        loss.backward()

        optimizer.step()

        total_loss += loss.item()

    print(
        f"Epoch {epoch+1} Loss: "
        f"{total_loss:.4f}"
    )

# SAVE LATENT EMBEDDINGS
with torch.no_grad():

    latent = model.embedding(X)

latent_df = pd.DataFrame(
    latent.numpy()
)

latent_df.to_csv(
    "results/tumor_transformer_embeddings.csv",
    index=False
)

print("\nSaved transformer embeddings.")