# CourseMate — AI Course Recommendation System

## Overview
CourseMate is a simple command-line recommendation system for Fundamental of AI/ML. It recommends courses from a small dataset using content-based filtering, TF-IDF and cosine similarity.

## Features
- Course dataset loading and validation
- User preference input
- TF-IDF vectorization
- Cosine similarity
- Top-5 recommendations
- Automated tests
- Command-line execution

## Technologies
Python 3.10+, pandas, scikit-learn, pytest.

## Structure
```text
CourseMate/
├── data/courses.csv
├── src/data_loader.py
├── src/recommender.py
├── src/main.py
├── tests/test_recommender.py
├── reports/
├── README.md
├── statement.md
└── requirements.txt
```

## Setup — Windows
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Run
```bash
python -m src.main
```

Example inputs:
```text
Skill: Python
Interest: Machine Learning
Level: beginner
```

The system displays five recommended courses.

## Test
```bash
python -m pytest -q
```

## How It Works
1. Load course information.
2. Combine domain, level and keywords.
3. Convert text to TF-IDF vectors.
4. Convert the user's preferences to a vector.
5. Calculate cosine similarity.
6. Sort courses by similarity and show the top five.

## Functional Modules
1. Data module
2. Recommendation module
3. User interaction module

## Non-Functional Requirements
- Usability
- Maintainability
- Reliability
- Resource efficiency
- Reproducibility

## Limitations
This is a basic content-based recommender. It does not use ratings, user history or collaborative filtering.

## Future Enhancements
Ratings, user history, collaborative filtering, larger dataset, and web interface.

## Author
**[VIKAS TIWARI]**
**[25MIM10105]**
Integrated M.Tech – AI/ML
VIT Bhopal University
