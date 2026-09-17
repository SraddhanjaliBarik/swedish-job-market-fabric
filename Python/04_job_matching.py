import pandas as pd
from pathlib import Path


# =========================================
# 1. Load job skills and CV skills
# =========================================

job_skills_file = Path("Data/processed/job_skills.csv")
cv_skills_file = Path("Data/processed/cv_skills.csv")

job_skills = pd.read_csv(job_skills_file)
cv_skills = pd.read_csv(cv_skills_file)


print("Job skill records:", len(job_skills))
print("CV skills:", len(cv_skills))


# =========================================
# 2. Get unique CV skills
# =========================================

cv_skill_set = set(
    cv_skills["skill"]
    .str.lower()
    .str.strip()
)


# =========================================
# 3. Add matching information
# =========================================

job_skills["skill_lower"] = (
    job_skills["skill"]
    .str.lower()
    .str.strip()
)

job_skills["skill_match"] = (
    job_skills["skill_lower"]
    .isin(cv_skill_set)
)


# =========================================
# 4. Calculate match for each job
# =========================================

job_match = (
    job_skills
    .groupby(
        ["job_id", "job_title", "company"],
        as_index=False
    )
    .agg(
        required_skills=("skill", "count"),
        matched_skills=("skill_match", "sum")
    )
)


# =========================================
# 5. Calculate Skill Coverage %
# =========================================

job_match["skill_coverage"] = (
    job_match["matched_skills"]
    / job_match["required_skills"]
    * 100
)


job_match["skill_coverage"] = job_match[
    "skill_coverage"
].round(1)


# =========================================
# 6. Create a simple match category
# =========================================

def match_category(coverage):

    if coverage >= 80:
        return "High Coverage"

    elif coverage >= 50:
        return "Medium Coverage"

    else:
        return "Low Coverage"


job_match["match_category"] = (
    job_match["skill_coverage"]
    .apply(match_category)
)


# =========================================
# 7. Find missing skills
# =========================================

def find_missing_skills(job_id):

    job_rows = job_skills[
        job_skills["job_id"] == job_id
    ]

    missing = job_rows[
        ~job_rows["skill_lower"].isin(cv_skill_set)
    ]["skill"].unique()

    return ", ".join(missing)


job_match["missing_skills"] = job_match[
    "job_id"
].apply(find_missing_skills)


# =========================================
# 8. Save results
# =========================================

output_folder = Path("Data/processed")

output_folder.mkdir(
    parents=True,
    exist_ok=True
)

output_file = (
    output_folder / "job_match_results.csv"
)

job_match.to_csv(
    output_file,
    index=False,
    encoding="utf-8-sig"
)


# =========================================
# 9. Display results
# =========================================

print("\nJob Match Results:")

print(
    job_match[
        [
            "job_id",
            "job_title",
            "company",
            "required_skills",
            "matched_skills",
            "skill_coverage",
            "match_category",
            "missing_skills"
        ]
    ].sort_values(
        "skill_coverage",
        ascending=False
    ).to_string(index=False)
)


print(f"\nResults saved to: {output_file}")