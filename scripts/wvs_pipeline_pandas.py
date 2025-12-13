import pandas as pd
import s3fs

print("=" * 60)
print("WVS Lakehouse Pipeline — Pandas (Bronze → Silver → Gold)")
print("=" * 60)

# =========================
# Connexion MinIO
# =========================
fs = s3fs.S3FileSystem(
    key="ROOTUSER",
    secret="CHANGEME123",
    client_kwargs={"endpoint_url": "http://localhost:9000"}
)

# =========================
# BRONZE
# =========================
bronze_path = "datalake/wvs/bronze/WVS_Cross-National_Wave_7_csv_v6_0.csv"

print("\n[1/3] Chargement Bronze...")
with fs.open(bronze_path, "rb") as f:
    df = pd.read_csv(f, low_memory=False)

print(f"✓ Bronze chargé : {df.shape[0]} lignes, {df.shape[1]} colonnes")

# =========================
# Sélection colonnes WVS
# =========================
COLUMN_MAP = {
    "country": "B_COUNTRY_ALPHA",
    "education_level": ["X025", "Q275", "EDUC"],
    "health_status": ["A009", "Q47", "HEALTH"],
    "employment_status": ["X028", "Q279", "EMPLOY"],
    "happiness": ["A008", "Q46", "HAPPY"]
}

def find_column(df, candidates):
    for c in candidates:
        for col in df.columns:
            if c.upper() == col.upper() or c.upper() in col.upper():
                return col
    return None

selected_cols = {}
for key, candidates in COLUMN_MAP.items():
    if isinstance(candidates, list):
        col = find_column(df, candidates)
    else:
        col = candidates if candidates in df.columns else None

    if col is None:
        raise ValueError(f"❌ Colonne introuvable pour {key}")
    selected_cols[key] = col

print("\nColonnes utilisées :")
for k, v in selected_cols.items():
    print(f"  {k} → {v}")

# =========================
# SILVER
# =========================
print("\n[2/3] Création Silver...")

silver_df = df[list(selected_cols.values())].dropna()
silver_df.columns = selected_cols.keys()

silver_path = "datalake/wvs/silver/individuals_cleaned.parquet"
with fs.open(silver_path, "wb") as f:
    silver_df.to_parquet(f, engine="pyarrow")

print(f"✓ Silver créé : {len(silver_df)} lignes")

# =========================
# GOLD
# =========================
print("\n[3/3] Création Gold...")

gold_tables = {
    "education": silver_df[["country", "education_level"]].drop_duplicates(),
    "health": silver_df[["country", "health_status", "happiness"]],
    "employment": silver_df[["country", "employment_status"]].drop_duplicates(),
    "social_values": silver_df[["country", "happiness"]]
}

for name, gdf in gold_tables.items():
    path = f"datalake/wvs/gold/{name}.parquet"
    with fs.open(path, "wb") as f:
        gdf.to_parquet(f, engine="pyarrow")
    print(f"  ✓ Gold {name} : {len(gdf)} lignes")

print("\n✓✓✓ PIPELINE TERMINÉ AVEC SUCCÈS ✓✓✓")
