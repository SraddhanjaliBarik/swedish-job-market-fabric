# Swedish Job Market – Job Matching & Analytics

## Overview

**JobMatch-Fabric** is an end-to-end data analytics project built to analyse Swedish job-market data and support job matching based on skills, experience, and job requirements.

The project combines **Python, Microsoft Fabric, SQL, Power BI, DAX, and KQL** to demonstrate a complete analytics workflow — from data ingestion and transformation to data modelling, analysis, and dashboard reporting.

The project was developed as a portfolio project to demonstrate practical skills in **Data Analytics, Business Intelligence, Microsoft Fabric, data transformation, and job-market analysis**.

---

## Project Objectives

The main objectives are to:

* Collect and process job-market data
* Clean and transform raw job information
* Extract and analyse required skills
* Create structured datasets for analytics
* Build a job-matching approach based on skills and job requirements
* Use Microsoft Fabric for data processing and analytics
* Create a Power BI dashboard for interactive analysis
* Identify trends in the Swedish job market

---

## Technologies Used

| Technology           | Purpose                                                       |
| -------------------- | ------------------------------------------------------------- |
| **Python**           | Data ingestion, cleaning, transformation and skill extraction |
| **Pandas**           | Data manipulation and analysis                                |
| **Microsoft Fabric** | Data engineering and analytics workflow                       |
| **Lakehouse**        | Storage and structured data processing                        |
| **Notebooks**        | Data transformation and analysis                              |
| **SQL**              | Data querying and analysis                                    |
| **KQL**              | Querying and analysing data                                   |
| **Power BI**         | Interactive dashboards and reporting                          |
| **DAX**              | Measures and analytical calculations                          |
| **Git & GitHub**     | Version control and project management                        |

---

## Project Architecture

The project follows a simplified **Bronze → Silver → Gold** data architecture.

```text
Job Market Data
       │
       ▼
Python Data Ingestion
       │
       ▼
Bronze Layer
Raw job-market data
       │
       ▼
Silver Layer
Cleaned and transformed data
       │
       ▼
Gold Layer
Analytics-ready datasets
       │
       ▼
Semantic Model
       │
       ▼
Power BI Dashboard
```

---

## Data Pipeline

### 1. Data Ingestion

Python is used to collect and prepare job-market data.

The ingestion process includes:

* Loading job-market data
* Processing raw JSON data
* Creating structured datasets
* Preparing data for further transformation

Main script:

```text
Python/01_api_ingestion.py
```

---

### 2. Skill Extraction

Job descriptions are processed to identify relevant technical and professional skills.

Examples include:

* Python
* SQL
* Power BI
* Microsoft Fabric
* Azure
* Data Engineering
* Data Analytics
* Machine Learning

Main script:

```text
Python/02_skill_extraction.py
```

---

### 3. CV Profile

A structured profile is created to represent candidate skills and experience.

Main script:

```text
Python/03_cv_profile.py
```

---

### 4. Job Matching

The project compares candidate skills with job requirements to support job matching.

The matching process considers:

* Required skills
* Candidate skills
* Skill overlap
* Job requirements
* Relevant technologies

Main script:

```text
Python/04_job_matching.py
```

---

## Microsoft Fabric

Microsoft Fabric is used to demonstrate a modern analytics workflow.

The project uses a layered approach:

### Bronze

Stores raw job-market data with minimal transformation.

### Silver

Contains cleaned and transformed data.

Typical transformations include:

* Removing duplicates
* Handling missing values
* Standardising fields
* Transforming data types
* Preparing structured job information

### Gold

Contains analytics-ready datasets used for reporting and analysis.

---

## SQL Analysis

SQL is used to analyse the processed job-market data.

Examples of analysis include:

* Jobs by location
* Jobs by category
* Most requested skills
* Job distribution by experience level
* Technology demand
* Skill frequency
* Job-market trends

SQL scripts are available in:

```text
Sql/
```

---

## DAX Analysis

DAX is used in Power BI to create analytical measures and KPIs.

Examples include:

* Total Jobs
* Jobs by Location
* Jobs by Experience Level
* Skill Demand
* Job Category Analysis
* Percentage distributions

DAX expressions are available in:

```text
DAX/
```

---

## Power BI Dashboard

The Power BI dashboard provides an interactive view of the Swedish job market.

The dashboard allows users to analyse:

* Total number of jobs
* Technical skills in demand
* Job categories
* Jobs by employment type
* Jobs by City
* Jobs published by month
* Jobs by Occupation
* Top 10 Companies by job count

Users can interact with filters and visuals to explore different parts of the job market.

## Measures
Total Jobs = COUNTROWS(gold_jobs)

Total Companies = DISTINCTCOUNT(gold_jobs[company])

SQL Jobs = CALCULATE([Total Jobs], gold_jobs[has_sql] = TRUE())

Power BI Jobs = CALCULATE([Total Jobs], gold_jobs[has_power_bi] = TRUE())

Python Jobs = CALCULATE([Total Jobs], gold_jobs[has_python] = TRUE())

Azure Jobs = CALCULATE([Total Jobs], gold_jobs[has_azure] = TRUE())

Databricks Jobs = CALCULATE([Total Jobs], gold_jobs[has_databricks] = TRUE())

Fabric Jobs = CALCULATE([Total Jobs], gold_jobs[has_fabric] = TRUE())

Dashboard screenshots are available in:

```text
power bi/
```

---

## Key Insights

The analysis can be used to identify:

* Which technical skills are frequently requested
* Which City have more job opportunities
* How job requirements vary by role
* Which skills are relevant for different job categories
* Patterns in the Swedish data and BI job market

---

## Project Structure

```text
JobMatch-Fabric/
│
├── Data/
│   ├── powerbi_jobs_clean.csv
│   ├── processed/
│   └── raw/
│       └── powerbi_jobs_raw.json
│
├── Python/
│   ├── 01_api_ingestion.py
│   ├── 02_skill_extraction.py
│   ├── 03_cv_profile.py
│   └── 04_job_matching.py
│
├── DAX/
│
├── Kql/
│
├── Sql/
│
├── notebook/
│   ├── Bronze_notebook.ipynb
│   ├── silver_Notebook.ipynb
│   └── Gold_notebook.ipynb
│
├── power bi/
│
├── docs/
│
├── screenshorts/
│
├── README.md
│
└── .gitignore
```

---

## Skills Demonstrated

This project demonstrates practical experience with:

* Data ingestion
* Data cleaning
* Data transformation
* Exploratory data analysis
* Python and Pandas
* SQL
* Data modelling
* Microsoft Fabric
* Lakehouse architecture
* Bronze/Silver/Gold architecture
* Power BI
* DAX
* KQL
* Data visualisation
* Git and GitHub

---

## Future Improvements

Possible future improvements include:

* Automating regular job-data ingestion
* Adding additional Swedish job sources
* Improving the job-matching algorithm
* Adding semantic similarity between CVs and job descriptions
* Introducing machine-learning-based job recommendations
* Adding real-time or scheduled data refresh
* Expanding the Power BI semantic model
* Adding Azure/Fabric pipeline orchestration

---

## Conclusion

JobMatch-Fabric demonstrates an end-to-end approach to working with job-market data, combining **Python, SQL, Microsoft Fabric and Power BI**.

The project focuses on transforming raw job information into structured, analytics-ready data and presenting the results through interactive business intelligence dashboards.

It serves as a practical portfolio example of **Data Analytics, BI Development, and Microsoft Fabric analytics workflows**.
