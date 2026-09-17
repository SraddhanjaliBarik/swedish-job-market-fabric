import pandas as pd
from pathlib import Path


# =========================================
# 1. Load cleaned job data
# =========================================

input_file = Path("Data/processed/powerbi_jobs_clean.csv")

jobs_df = pd.read_csv(input_file)

print("Number of jobs:", len(jobs_df))


# =========================================
# 2. Define skills to search for
# =========================================

skills = {
    "Power BI": ["power bi"],
    "Power BI Desktop": ["power bi desktop", "pbi desktop"],
    "PBIRS": ["pbirs", "power bi report server"],
    "DAX": ["dax"],
    "SQL": ["sql"],
    "Python": ["python"],
    "SSAS": ["ssas", "sql server analysis services"],
    "Tableau": ["tableau"],
    "Microsoft Fabric": ["microsoft fabric", "ms fabric", "fabric"],
    "Azure": ["azure", "microsoft azure"],
    "Data Modeling": ["data model", "data modeling", "datamodell"],
    "Data Warehouse": ["data warehouse", "data warehouse"],
    "Power Query": ["power query"],
    "Excel": ["excel"],
    "Grafana": ["grafana"],
    "PySpark": ["pyspark"],
    "Spark": ["apache spark", "spark"],
    "Git": ["git", "github"],
    "SSIS": ["ssis"],
}


# =========================================
# 3. Extract skills from job descriptions
# =========================================

skill_records = []

for _, job in jobs_df.iterrows():

    description = str(job["description"]).lower()

    for skill_name, keywords in skills.items():

        for keyword in keywords:

            if keyword in description:

                skill_records.append({
                    "job_id": job["job_id"],
                    "job_title": job["job_title"],
                    "company": job["company"],
                    "skill": skill_name
                })

                break


# =========================================
# 4. Create skill DataFrame
# =========================================

job_skills_df = pd.DataFrame(skill_records)


# =========================================
# 5. Remove duplicates
# =========================================

job_skills_df = job_skills_df.drop_duplicates(
    subset=["job_id", "skill"]
)


# =========================================
# 6. Save skill data
# =========================================

output_folder = Path("Data/processed")

output_folder.mkdir(
    parents=True,
    exist_ok=True
)

output_file = output_folder / "job_skills.csv"

job_skills_df.to_csv(
    output_file,
    index=False,
    encoding="utf-8-sig"
)


# =========================================
# 7. Display results
# =========================================

print("\nSkills extracted:")
print(job_skills_df.shape)

print("\nFirst 20 records:")

print(
    job_skills_df.head(20).to_string(index=False)
)


# =========================================
# 8. Most requested skills
# =========================================

print("\nMost requested skills:")

skill_summary = (
    job_skills_df
    .groupby("skill")
    .size()
    .sort_values(ascending=False)
)

print(skill_summary)


print(f"\nSkill data saved to: {output_file}")