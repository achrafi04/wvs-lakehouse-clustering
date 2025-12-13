from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

print("=" * 60)
print("WVS GOLD — K-MEANS CLUSTERING (K=3)")
print("=" * 60)

# =========================
# CONFIG
# =========================
BASE = Path(r"C:/minio/data/datalake/wvs/pandas/gold")
OUTPUT = Path("outputs")
OUTPUT.mkdir(exist_ok=True)

# =========================
# 1️⃣ Chargement des données
# =========================
print("\n[1/4] Chargement des données GOLD...")

df = pd.read_parquet(BASE / "gold_country_profile.parquet")

features = [
    "mean_happiness",
    "mean_health",
    "mean_education",
    "employment_diversity"
]

X = df[features]

print(f"✓ Données chargées : {X.shape}")

# =========================
# 2️⃣ Normalisation
# =========================
print("\n[2/4] Normalisation des variables...")

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# =========================
# 3️⃣ K-Means
# =========================
print("\n[3/4] Clustering K-Means (k=3)...")

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df["cluster"] = kmeans.fit_predict(X_scaled)

print("✓ Clustering terminé")

# =========================
# 4️⃣ Analyse
# =========================
print("\n[4/4] Analyse des clusters\n")

cluster_summary = df.groupby("cluster")[features].mean()
print(cluster_summary)

print("\nRépartition des pays par cluster :")
print(df["cluster"].value_counts())

# =========================
# 📊 GRAPHIQUES
# =========================

# Scatter (2 dimensions)
plt.figure(figsize=(8, 5))
plt.scatter(
    X_scaled[:, 0], 
    X_scaled[:, 1], 
    c=df["cluster"], 
    cmap="Set1", 
    s=60
)
plt.xlabel("Bonheur (normalisé)")
plt.ylabel("Santé (normalisée)")
plt.title("K-Means Clustering des pays (k=3)")
plt.colorbar(label="Cluster")
plt.tight_layout()
plt.savefig(OUTPUT / "kmeans_clusters_scatter.png")
plt.close()

# Distribution des clusters
plt.figure(figsize=(6, 4))
df["cluster"].value_counts().sort_index().plot(kind="bar")
plt.xlabel("Cluster")
plt.ylabel("Nombre de pays")
plt.title("Distribution des pays par cluster")
plt.tight_layout()
plt.savefig(OUTPUT / "cluster_distribution.png")
plt.close()

print("\n✓ Graphiques générés :")
print("  - outputs/kmeans_clusters_scatter.png")
print("  - outputs/cluster_distribution.png")

# =========================
# 💾 Sauvegarde
# =========================
df.to_parquet(BASE / "country_profiles_clustered.parquet", index=False)
print("\n✓ Clusters sauvegardés")

print("\n✓✓✓ CLUSTERING TERMINÉ AVEC SUCCÈS ✓✓✓")
