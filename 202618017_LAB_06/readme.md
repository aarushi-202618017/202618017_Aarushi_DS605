**DS605 FUNDAMENTALS OF MACHINE LEARNING MSc DS** 

**Student Id: 202618017**

Student Name: Aarushi Rana

**Lab 06 Description:**

## Overall Conclusions and Observations

This repository covers two distinct classification tasks: **Asphalt Pavement Crack Detection** (Part A) and **Email Spam Classification** (Part B).

### Part A: Asphalt Pavement Crack Detection
For image-based crack detection, we extracted features like brightness, contrast, and edge density. The **Random Forest Classifier** was most effective:
- **Accuracy**: 96.25%
- **F1-Score**: 96.30%

### Part B: Email Spam Classification
For spam detection using word counts, we evaluated multiple models:

- **Best Overall Balanced System:** Raw Count Logistic Regression (Pipeline 1) for highest F1-Score (0.9704) and accuracy (98.26%) with minimal false positives.
- **Best High-Throughput / Speed System:** Scaled 1,000 Chi2 Features Logistic Regression (Pipeline 2) offering fast inference while maintaining high accuracy.
- **Best Security / Catch-All System:** Log-Scaled + L2 Norm + Balanced Logistic Regression (Pipeline 3) for highest Recall (98.67%), ideal for identifying critical spam.

### Summary
Both tasks highlight the critical role of appropriate feature engineering and model selection, demonstrating effective machine learning solutions tailored to specific data types and performance goals.
