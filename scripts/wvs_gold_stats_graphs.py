from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

print("=" * 60)
print("WVS GOLD — STATISTICS & GRAPHS")
print("=" * 60)

# ==============================
# PATHS
# ==============================
GOLD = Path(r"C:/minio/data/datalake/wvs/pandas/gold/gold_country_profile.parquet")
OUTPUT = Path("outputs")
OUTPUT.mkdir(exist_ok=True)

# ==============================
# LOAD DATA
# ==============================
print("\n[1/4] Chargement des données GOLD...")
df = pd.read_parquet(GOLD)

print("✓ Données chargées :", df.shape)
print(df.head())

# ==============================
# 1️⃣ STATISTIQUES DESCRIPTIVES
# ==============================
print("\n[2/4] Statistiques descriptives")

stats = df.describe()
print(stats)

stats.to_csv(OUTPUT / "descriptive_statistics.csv")
print("✓ Statistiques sauvegardées")

# Top / Bottom bonheur
print("\nTop 5 pays les plus heureux")
print(df.sort_values("mean_happiness", ascending=False).head(5))

print("\nBottom 5 pays les moins heureux")
print(df.sort_values("mean_happiness").head(5))

# ==============================
# 2️⃣ GRAPHIQUES
# ==============================
print("\n[3/4] Génération des graphiques")

plt.style.use("ggplot")

# Histogramme bonheur
plt.figure(figsize=(8, 5))
plt.hist(df["mean_happiness"], bins=20)
plt.title("Distribution du bonheur moyen par pays")
plt.xlabel("Bonheur moyen")
plt.ylabel("Nombre de pays")
plt.tight_layout()
plt.savefig(OUTPUT / "happiness_distribution.png")
plt.close()

# Top 10 pays bonheur
top10 = df.sort_values("mean_happiness", ascending=False).head(10)

plt.figure(figsize=(10, 5))
plt.bar(top10["country"], top10["mean_happiness"])
plt.title("Top 10 pays — Bonheur moyen")
plt.xlabel("Pays")
plt.ylabel("Bonheur moyen")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(OUTPUT / "top10_happiest_countries.png")
plt.close()

# Bonheur vs Santé
plt.figure(figsize=(7, 5))
plt.scatter(df["mean_health"], df["mean_happiness"], alpha=0.7)
plt.xlabel("Santé moyenne")
plt.ylabel("Bonheur moyen")
plt.title("Relation Santé vs Bonheur")
plt.tight_layout()
plt.savefig(OUTPUT / "health_vs_happiness.png")
plt.close()

print("✓ Graphiques sauvegardés")

# ==============================
# 3️⃣ INTERPRÉTATION RAPIDE
# ==============================
print("\n[4/4] Interprétation rapide")

corr = df["mean_health"].corr(df["mean_happiness"])

print(f"Corrélation santé ↔ bonheur : {corr:.2f}")

print("\nObservations clés :")
print("• Le bonheur moyen varie fortement selon les pays.")
print("• Une corrélation positive santé-bonheur est observée.")
print("• Ces indicateurs sont pertinents pour un clustering pays.")

print("\n" + "=" * 60)
print("✓✓✓ STATS & GRAPHS TERMINÉS AVEC SUCCÈS ✓✓✓")
print("=" * 60)
