# Bronze Layer — Raw Data

## Description
The Bronze layer contains the **raw, unprocessed data** ingested into the data lake.
In this project, it corresponds to the original CSV file from the **World Values Survey (WVS) – Wave 7**.

## Content
- Original WVS CSV file
- No transformation or cleaning applied
- Data is stored exactly as provided by the source

## Purpose
The Bronze layer serves as:
- A **single source of truth**
- A historical backup of the original data
- The entry point of the data pipeline

## Notes
Due to size constraints, raw data files are **not included in this repository**.
They can be regenerated or downloaded from the official WVS website.
