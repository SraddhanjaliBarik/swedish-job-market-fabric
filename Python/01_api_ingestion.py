import requests
import json
import csv
from pathlib import Path
import pandas as pd


# =========================================
# 1. Get jobs from JobTech API
# =========================================

url = "https://jobsearch.api.jobtechdev.se/search"

params = {
    "q": "Power BI",
    "limit": 20
}

response = requests.get(url, params=params)

print("Status:", response.status_code)

response.raise_for_status()

data = response.json()

print("Available keys:", data.keys())
print("Number of jobs:", len(data["hits"]))


# =========================================
# 2. Save RAW API data
# =========================================

raw_folder = Path("Data/raw")
raw_folder.mkdir(parents=True, exist_ok=True)

raw_file = raw_folder / "powerbi_jobs_raw.json"

with open(raw_file, "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)

print(f"\nRaw data saved to: {raw_file}")


# =========================================
# 3. Convert API data to DataFrame
# =========================================

jobs_df = pd.json_normalize(data["hits"])

print("\nDataFrame shape:")
print(jobs_df.shape)

print("\nColumns:")
print(jobs_df.columns.tolist())


# =========================================
# 4. Select useful columns
# =========================================

jobs_clean = jobs_df[
    [
        "id",
        "headline",
        "description.text",
        "employer.name",
        "publication_date",
        "application_deadline",
        "employment_type.label",
        "working_hours_type.label",
        "duration.label",
        "workplace_model.label",
        "workplace_address.city",
        "workplace_address.region",
        "workplace_address.country",
        "occupation.label",
        "occupation_field.label",
        "webpage_url"
    ]
].copy()


# =========================================
# 5. Rename columns
# =========================================

jobs_clean = jobs_clean.rename(columns={
    "id": "job_id",
    "headline": "job_title",
    "description.text": "description",
    "employer.name": "company",
    "employment_type.label": "employment_type",
    "working_hours_type.label": "working_hours",
    "duration.label": "duration",
    "workplace_model.label": "workplace_model",
    "workplace_address.city": "city",
    "workplace_address.region": "region",
    "workplace_address.country": "country",
    "occupation.label": "occupation",
    "occupation_field.label": "occupation_field",
    "webpage_url": "job_url"
})


# =========================================
# 6. Convert dates
# =========================================

jobs_clean["publication_date"] = pd.to_datetime(
    jobs_clean["publication_date"],
    errors="coerce"
)

jobs_clean["application_deadline"] = pd.to_datetime(
    jobs_clean["application_deadline"],
    errors="coerce"
)


# =========================================
# 7. Remove duplicate jobs
# =========================================

jobs_clean = jobs_clean.drop_duplicates(
    subset="job_id"
)


# =========================================
# 8. Save CLEAN data
# =========================================

processed_folder = Path("Data/processed")
processed_folder.mkdir(parents=True, exist_ok=True)

output_file = processed_folder / "powerbi_jobs_clean.csv"

# QUOTE_ALL keeps multiline descriptions and commas
# inside one CSV field.
jobs_clean.to_csv(
    output_file,
    index=False,
    encoding="utf-8-sig",
    quoting=csv.QUOTE_ALL,
    lineterminator="\n"
)


# =========================================
# 9. Show result
# =========================================

print("\nClean dataset:")
print(jobs_clean.shape)

print("\nFirst 5 jobs:")

print(
    jobs_clean[
        [
            "job_id",
            "job_title",
            "company",
            "city",
            "occupation"
        ]
    ].head()
)

print(f"\nClean data saved to: {output_file}")

