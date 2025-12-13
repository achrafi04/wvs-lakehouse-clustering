# Gold Layer — Analytical Country Profiles

## Description
The Gold layer contains **aggregated, analytics-ready datasets**
built from the Silver layer.

Each record represents a **country-level profile** derived from individual responses.

## Aggregated Indicators
For each country:
- Mean happiness
- Mean perceived health
- Mean education level
- Employment diversity
- Population size

## Content
- Country-level Parquet files
- Features optimized for:
  - Visualization
  - Statistical analysis
  - Machine learning (clustering)

## Purpose
The Gold layer is used for:
- Cross-country comparisons
- K-Means clustering
- Policy-oriented analysis
- Decision support

## Modeling
- Standardized features
- Unsupervised learning (K-Means, k=3)

## Notes
The Gold layer represents the **final business-ready data** of the Lakehouse pipeline.
