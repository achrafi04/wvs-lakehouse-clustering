# Data Directory

This folder contains the Lakehouse layers used in the project.

- `bronze/` → raw data (CSV)
- `silver/` → cleaned individual-level data (Parquet)
- `gold/` → aggregated country-level datasets (Parquet)

Each layer is immutable once generated.
