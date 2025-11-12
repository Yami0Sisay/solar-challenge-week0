# Solar Challenge Week 0
## Overview

Repo purpose: set up a reproducible Python environment, use Git properly (branches + PRs), and perform initial data profiling, cleaning, and EDA for country datasets (Benin, Togo; Sierra Leone next).

The goal of this task is to:
- Create a clean, version-controlled Python setup.
- Profile datasets and report missing values and types.
- Clean data (Z-score outlier removal, median imputation).
- Run EDA (time series, correlations, wind/temperature relations).
- Export cleaned CSVs locally in data/ (never committed).

---

## Task-1. Environment Setup

Follow these steps to reproduce the environment exactly as configured in this project:

### 1️. Clone the Repository
``` bash
git clone https://github.com/<your-username>/solar-challenge-week0.git
cd solar-challenge-week0
```
### 2. Open the Project in Visual Studio Code

### 3. Virtual Environement 
``` bash
# Create a virtual environment
python -m venv .venv

# Activate the virtual environment (PowerShell)
.venv\Scripts\activate

#If activation is blocked, run the following once
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\activate

# OR (for Linux/Mac)
source .venv/bin/activate
```
### 4. Install Required Packages 
```bash
pip install pandas
pip freeze > requirements.txt
```
## Steps Followed 
1. Repostiory Creation 
A new GitHub repository named solar-challenge-week0 was created with an initial README file.

2. Local Setup
The repository was cloned locally using HTTPS. The folder was opened in Visual Studio Code to begin the setup process.

3. Environment Setup
A Python virtual environment (.venv) was created and activated. A .gitignore file was added to exclude the virtual environment and the data/ folder from version control.

4. File and Folder Structure
A notebooks/ folder was created with an __init__.py file and a sample Jupyter Notebook named solar_challenge.ipynb.
A data/ folder was created to store datasets (excluded from Git).
A src/ folder was added with an __init__.py file for source code.
A requirements.txt file was created to record dependencies using pip freeze.

5. Dependency Installation
The pandas library was installed and the dependencies were captured in requirements.txt.

6. Branch Creation and Workflow Setup
A new branch named setup-task was created using:
```bash
git branch setup-task
git checkout setup-task
```
A .github/workflows/unittests.yml file was added to set up a basic GitHub Actions CI workflow that verifies Python installation and dependency setup.

7. Continuous Integration (GitHub Actions)
A basic GitHub Actions workflow was created under .github/workflows/unittests.yml to ensure that the environment installs correctly.

8. Commit and Merge
Changes were committed with meaningful messages.
The setup-task branch was then pushed to GitHub, and a Pull Request was created and merged into the main branch.

## Task 2. Data Profiling, Cleaning and EDA

Follow these steps to reproduce the data profiling, cleaning, and EDA process conducted for the country datasets.

### 1️. Branch Creation

A new branch was created for the Benin dataset EDA and cleaning task using:
```bash
git checkout -b eda-country # country = benin/togo/sierraleone
```

### 2. Dataset Preparation

Each country’s dataset was downloaded and stored inside the data/ folder (excluded from Git).

### 3. Data Loading and Inspection

The dataset was imported into a Jupyter notebook using pandas:
```bash
import pandas as pd
Benin = pd.read_csv("../data/benin-malanville.csv")
print(Benin.shape)
Benin.head()
```

The Timestamp column was converted from object to datetime for accurate time-series analysis:
```bash
Benin["Timestamp"] = pd.to_datetime(Benin["Timestamp"], errors="coerce")
```

Basic structure, data types, and null counts were inspected using:
```bash
Benin.info()
Benin.describe()
```

Columns with more than 5 % missing values were listed and reviewed.
```bash
Benin.isna().sum()
```
### 4. Outlier Detection and Cleaning

Outliers were identified using the Z-score method (|Z| > 3) on solar and wind parameters:
GHI, DNI, DHI, ModA, ModB, WS, WSgust.
Missing values in key columns (GHI, DNI, DHI, ModA, ModB, WS, WSgust, RH, Tamb) were imputed with median values.

```bash
from scipy import stats
import numpy as np

target_cols = ['GHI','DNI','DHI','ModA','ModB','WS','WSgust']
z = np.abs(stats.zscore(Benin[target_cols], nan_policy="omit"))
Benin_clean = Benin[(z < 3).all(axis=1)].copy()

for c in target_cols + ['RH','Tamb']:
    if c in Benin_clean.columns:
        Benin_clean[c] = Benin_clean[c].fillna(Benin_clean[c].median())
```

The cleaned dataset was exported locally as:
```bash
data/benin_clean.csv
```

### 5. Time-Series and Correlation Analysis

Using matplotlib and seaborn, time-series plots were generated for: GHI, DNI, DHI, and Tamb against Timestamp to observe daily and monthly solar patterns.

Correlation heatmaps and scatter plots were also created to study: GHI, DNI, DHI, TModA, TModB, Relationships such as WS vs GHI, RH vs Tamb, and RH vs GHI.

### 6. Distribution and Wind Analysis

Wind-rose and histograms were plotted to examine wind direction and speed distributions.

Histograms for GHI and WS visualized irradiance and wind variability.

### 7. Temperature and Humidity Relationship

Scatter plots between Relative Humidity (RH) and Temperature (Tamb) were analyzed to understand their effect on solar radiation (GHI).

### 8. Bubble Chart Visualization

A bubble chart was produced with:
X-axis: Tamb
Y-axis: GHI
Bubble size: RH or BP (depending on availability)

And tThis visualization showed how humidity or pressure correlates with solar irradiance.

### 9. Cleaning Impact Review

For datasets containing a Cleaning flag, average ModA and ModB values were compared pre- and post-cleaning to measure sensor performance improvement.

### 10. Commit and Merge

After completing the  analysis the files were commited to each branch and a Pull Request was opened and merged into the main branch.





## Folder Structure
```bash
solar-challenge-week0/
│
├── .github/
│   └── workflows/
│       └── unittests.yml
│
├── .vscode/
│   └── settings.json
│
├── data/
│
├── notebooks/
│   ├── __init__.py
│   ├── benin_eda.ipynb
│   ├── sierraleone_eda.ipynb
│   ├── togo_eda.ipynb
│   └── README.md
│
├── scripts/
│   ├── __init__.py
│   └── README.md
│
├── src/
│   └── __init__.py
│
├── tests/
│   └── __init__.py
│
├── .gitignore
├── README.md 
└── requirements.txt
```

Live Dashboard
Streamlit App: https://your-streamlit-link-here.streamlit.app