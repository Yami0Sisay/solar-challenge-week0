# Solar Challenge Week 0 - Environement & Git Setup
## Overview

This repository was created as part of **10 Academy’s Solar Challenge (Week 0)** to practice professional Git workflows, environment setup, and project structuring before beginning data-related tasks.

The goal of this task is to:
- Set up a proper **Python virtual environment**.
- Practice **branching, committing, and merging** via **Git & GitHub**.
- Configure a **basic CI workflow** with GitHub Actions.
- Document the setup process for reproducibility.

---

## Environment Setup Instructions

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


## Folder Structure
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
│   └── solar_challenge.ipynb
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


