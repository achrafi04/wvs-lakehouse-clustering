# 🌍 Socio-Economic Country Profiling using a Lakehouse Architecture

**World Values Survey (WVS) — Data Analytics & Clustering Project**

## 📌 Project Overview

This project proposes a **data-driven socio-economic analysis of countries** based on the **World Values Survey (WVS – Wave 7)**.
Using a **Lakehouse architecture (Bronze–Silver–Gold)** combined with **statistical analysis and unsupervised machine learning**, we cluster countries according to multidimensional well-being indicators.

The goal is to move beyond traditional economic metrics and provide a **holistic country profiling framework** integrating happiness, health perception, education, and employment structure.

---

## 🎯 Problem Statement

Economic indicators such as GDP fail to capture **subjective well-being** and social perception.
This project addresses the following research question:

> **How can countries be objectively grouped based on multidimensional well-being indicators derived from large-scale survey data?**

---

## 🧠 Methodology Summary

### 1️⃣ Lakehouse Architecture

The pipeline follows the **Bronze → Silver → Gold** paradigm:

| Layer  | Description                       |
| ------ | --------------------------------- |
| Bronze | Raw WVS CSV data                  |
| Silver | Cleaned individual-level data     |
| Gold   | Aggregated country-level profiles |

---

### 2️⃣ Feature Engineering

Each country is represented by the following indicators:

* Mean happiness
* Mean perceived health
* Mean education level
* Employment diversity
* Population size

---

### 3️⃣ Statistical Analysis

* Descriptive statistics
* Country ranking by happiness
* Correlation analysis (health ↔ happiness)
* Distribution analysis

---

### 4️⃣ Machine Learning

* **K-Means clustering (k = 3)**
* Feature standardization
* Cluster interpretation and labeling

---

## 📊 Key Results

### 🔹 Statistical Insights

* Significant variability in happiness across countries
* Positive correlation between health perception and happiness
* Education level alone does not guarantee higher well-being

### 🔹 Clustering Outcome

Three meaningful socio-economic country profiles were identified:

* **Cluster 0**: High happiness & health
* **Cluster 1**: Intermediate socio-economic profile
* **Cluster 2**: High education but lower happiness

---

## 📈 Visual Outputs

All generated figures are stored in the `outputs/` directory:

```
outputs/
├── happiness_distribution.png
├── top10_happiest_countries.png
├── kmeans_clusters_scatter.png
├── cluster_distribution.png
```

---

## 📂 Repository Structure

```
.
├── data/
│   ├── bronze/
│   │   └── README.md
│   ├── silver/
│   │   └── README.md
│   └── gold/
│       └── README.md
│
├── scripts/
│   ├── wvs_pipeline_pandas.py
│   ├── wvs_pipeline_pandas_silver.py
│   ├── wvs_gold_stats_graphs.py
│   ├── wvs_gold_clustering.py
│   └── wvs_export_country_clusters.py
│
├── outputs/
│   ├── happiness_distribution.png
│   ├── top10_happiest_countries.png
│   ├── kmeans_clusters_scatter.png
│   └── cluster_distribution.png
│
├── report/
│   └── WVS_Lakehouse_Clustering_Report.tex
│
└── README.md
```

---

## 🛠 Technologies Used

* **Python**
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Parquet (PyArrow)
* MinIO (local object storage)
* LaTeX (scientific reporting)

---

## 🧪 Reproducibility

1. Download WVS Wave 7 dataset
2. Place raw CSV in `data/bronze/`
3. Run the pipeline scripts in order:

   ```bash
   python wvs_pipeline_pandas.py
   python wvs_pipeline_pandas_silver.py
   python wvs_gold_stats_graphs.py
   python wvs_gold_clustering.py
   ```
4. Generated datasets and figures will appear automatically

---

## 📌 Recommendations

* Integrate subjective indicators into policy evaluation frameworks
* Use cluster-based benchmarking between similar countries
* Extend the analysis to temporal trends across multiple WVS waves

---

## 👨‍🎓 Authors

* **Achraf IKISSE**
* **Ammar KASBAOUI**
* **Ilias ISSAF**

**Université Internationale de Rabat**
School of Computer Science
Academic Year 2025–2026

---

## 📜 License

This project is intended for **academic and educational purposes**.

---

### 🚀 Final Note

This repository demonstrates a **complete end-to-end data analytics pipeline**, from raw data ingestion to advanced clustering and scientific reporting.
