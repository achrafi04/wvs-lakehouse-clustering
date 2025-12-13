from pathlib import Path
import pandas as pd

print("=" * 60)
print("WVS Pandas Pipeline — SILVER")
print("=" * 60)

# ==============================
# PATHS
# ==============================
BRONZE = Path(r"C:/wvs/data/WVS_Cross-National_Wave_7_csv_v6_0.csv")
SILVER_DIR = Path(r"C:/minio/data/datalake/wvs/pandas/silver")
SILVER_DIR.mkdir(parents=True, exist_ok=True)

# ==============================
# LOAD BRONZE
# ==============================
print("\n[1/3] Chargement Bronze CSV...")
df = pd.read_csv(BRONZE, low_memory=False)
print(f"✓ Bronze chargé : {df.shape[0]} lignes, {df.shape[1]} colonnes")

# ==============================
# SELECT & RENAME
# ==============================
print("\n[2/3] Création Silver...")

silver = df[[
    "B_COUNTRY_ALPHA",  # country
    "Q275",             # education
    "Q47",              # health
    "Q279",             # employment
    "Q46"               # happiness
]].rename(columns={
    "B_COUNTRY_ALPHA": "country",
    "Q275": "education_level",
    "Q47": "health_status",
    "Q279": "employment_status",
    "Q46": "happiness"
})

# Drop missing values
silver = silver.dropna()

print(f"✓ Silver nettoyé : {silver.shape[0]} lignes")

# ==============================
# SAVE SILVER
# ==============================
silver_path = SILVER_DIR / "individuals_cleaned.parquet"
silver.to_parquet(silver_path, index=False)

print(f"✓ Silver sauvegardé → {silver_path}")
print("\n✓✓✓ SILVER TERMINÉ AVEC SUCCÈS ✓✓✓")
