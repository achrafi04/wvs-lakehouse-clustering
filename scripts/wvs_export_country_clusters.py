from pathlib import Path
import pandas as pd

print("=" * 60)
print("WVS — EXPORT COUNTRY CLUSTERS (FINAL)")
print("=" * 60)

# =========================
# CONFIG
# =========================
BASE = Path(r"C:/minio/data/datalake/wvs/pandas/gold")
OUTPUT = Path("outputs")
OUTPUT.mkdir(exist_ok=True)

STATS_FILE = BASE / "gold_country_profile.parquet"
CLUSTER_FILE = BASE / "country_profiles_clustered.parquet"
OUTPUT_FILE = OUTPUT / "wvs_country_clusters.csv"

CLUSTER_LABELS = {
    0: "High well-being countries",
    1: "Intermediate well-being countries",
    2: "Educated but less happy countries"
}

# =========================
# LOAD DATA
# =========================
print("\n[1/3] Chargement des données GOLD...")
stats = pd.read_parquet(STATS_FILE)
clusters = pd.read_parquet(CLUSTER_FILE)

print("✓ Stats :", stats.shape)
print("✓ Clusters :", clusters.shape)

# =========================
# MERGE
# =========================
print("\n[2/3] Fusion stats + clusters...")
df = stats.merge(
    clusters[["country", "cluster"]],
    on="country",
    how="left"
)

df["profile_label"] = df["cluster"].map(CLUSTER_LABELS)

df = df[
    [
        "country",
        "cluster",
        "profile_label",
        "mean_happiness",
        "mean_health",
        "mean_education",
        "employment_diversity",
        "population"
    ]
]

# =========================
# EXPORT
# =========================
print("\n[3/3] Export CSV...")
df.to_csv(OUTPUT_FILE, index=False, sep=";")

print(f"\n✓ CSV généré : {OUTPUT_FILE.resolve()}")
print("\n✓✓✓ EXPORT TERMINÉ AVEC SUCCÈS ✓✓✓")
