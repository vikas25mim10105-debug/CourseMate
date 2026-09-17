# CourseMate — Project Report
## 1. Cover Page
Project: CourseMate — AI Course Recommendation System
Course: Fundamental of AI/ML
Student: [VIKAS TIWARI]
registration no: [25MIM110105]
Program: Integrated M.Tech – AI/ML
Institution: VIT Bhopal University
Academic Year: 2026–27

## 2. Introduction
CourseMate is a command-line content-based recommendation system that recommends technical courses according to a user's skill, interest and preferred level.

## 3. Problem Statement
Students have many courses available and may need help identifying courses related to their current interests.

## 4. Objectives
- Build a simple recommendation system.
- Apply TF-IDF vectorization.
- Apply cosine similarity.
- Rank and display relevant courses.

## 5. Functional Requirements
Load data, check the data take in the preferences make TF-IDF vectors figure out the similarity sort the courses and show the five.

## 6. Non-Functional Requirements
Usability, maintainability, reliability, resource efficiency and reproducibility.

## 7. System Architecture
See reports/architecture.md.

## 8. Design Diagrams
See reports/workflow.md and reports/uml.md.

## 9. Dataset
The bundled CSV contains 20 technical course records with course name, domain, level and keywords.

## 10. Algorithm
Content-based filtering is used. TF-IDF converts course text into vectors. Cosine similarity compares the user profile vector with each course vector. Courses are then ranked by similarity.

## 11. Implementation
data_loader.py loads data. Recommender.py performs TF-IDF and similarity calculations. Main.py handles interaction.

## 12. Testing
Two pytest tests verify the dataset and recommendation output.

## 13. Challenges
Creating useful keywords, representing text numerically, ranking courses, and keeping the application terminal-based.

## 14. Learnings
TF-IDF, vector representation, cosine similarity, content-based recommendation, ranking, modular Python and testing.

## 15. Future Enhancements
Add ratings, user history, collaborative filtering, more courses and a web interface.

## 16. References
Python, pandas and scikit-learn documentation.
