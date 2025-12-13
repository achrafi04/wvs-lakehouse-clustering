# Silver Layer — Cleaned Individual Data

## Description
The Silver layer contains **cleaned and standardized individual-level data**
derived from the Bronze layer.

## Processing Steps
- Selection of relevant variables:
  - Country
  - Happiness
  - Health perception
  - Education level
  - Employment status
- Removal of missing or invalid values
- Harmonization of column names
- Conversion to Parquet format for efficient access

## Content
- Cleaned individual responses
- One row per individual
- Structured and analysis-ready

## Purpose
The Silver layer is designed for:
- Exploratory data analysis
- Statistical analysis
- Feature engineering for aggregation and modeling

## Storage Format
- Parquet (columnar, compressed, efficient for analytics)

## Notes
Silver data is generated automatically by running the pipeline scripts.
