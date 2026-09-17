import pandas as pd
from pathlib import Path


# =========================================
# 1. Create CV skill profile
# =========================================

cv_skills = [
    {
        "candidate_id": "candidate_001",
        "skill": "Power BI",
        "skill_category": "BI & Visualization",
        "years_experience": 2
    },
    {
        "candidate_id": "candidate_001",
        "skill": "Power BI Desktop",
        "skill_category": "BI & Visualization",
        "years_experience": 2
    },
    {
        "candidate_id": "candidate_001",
        "skill": "DAX",
        "skill_category": "BI & Visualization",
        "years_experience": 2
    },
    {
        "candidate_id": "candidate_001",
        "skill": "Power Query",
        "skill_category": "BI & Data Transformation",
        "years_experience": 2
    },
    {
        "candidate_id": "candidate_001",
        "skill": "SQL",
        "skill_category": "Data",
        "years_experience": 4
    },
    {
        "candidate_id": "candidate_001",
        "skill": "Python",
        "skill_category": "Programming",
        "years_experience": 2
    },
    {
        "candidate_id": "candidate_001",
        "skill": "PySpark",
        "skill_category": "Big Data",
        "years_experience": 1
    },
    {
        "candidate_id": "candidate_001",
        "skill": "Microsoft Fabric",
        "skill_category": "Data Platform",
        "years_experience": 1
    },
    {
        "candidate_id": "candidate_001",
        "skill": "Azure",
        "skill_category": "Cloud",
        "years_experience": 1
    },
    {
        "candidate_id": "candidate_001",
        "skill": "Tableau",
        "skill_category": "BI & Visualization",
        "years_experience": 3
    },
    {
        "candidate_id": "candidate_001",
        "skill": "Grafana",
        "skill_category": "Visualization",
        "years_experience": 1
    },
    {
        "candidate_id": "candidate_001",
        "skill": "Git",
        "skill_category": "Development",
        "years_experience": 1
    },
    {
        "candidate_id": "candidate_001",
        "skill": "Excel",
        "skill_category": "Analytics",
        "years_experience": 5
    }
]


# =========================================
# 2. Create DataFrame
# =========================================

cv_df = pd.DataFrame(cv_skills)


# =========================================
# 3. Save CV profile
# =========================================

output_folder = Path("Data/processed")

output_folder.mkdir(
    parents=True,
    exist_ok=True
)

output_file = output_folder / "cv_skills.csv"

cv_df.to_csv(
    output_file,
    index=False,
    encoding="utf-8-sig"
)


# =========================================
# 4. Display profile
# =========================================

print("\nCV Skill Profile:")
print(cv_df.to_string(index=False))

print("\nNumber of CV skills:", len(cv_df))

print(f"\nCV profile saved to: {output_file}")