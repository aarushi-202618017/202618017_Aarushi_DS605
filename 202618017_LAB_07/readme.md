PCA-Based Face Recognition

A computer vision project implementing facial representation, dimensionality reduction via Principal Component Analysis (PCA) using pure NumPy linear algebra, Euclidean similarity matching, and benchmark classification using traditional machine learning models.


Key Summary & Observations
Dimensionality Reduction: Retaining k = 100 principal components preserves >= 90% of total dataset variance, enabling significant storage compression while retaining core facial geometry.

PCA Space Matching: Nearest-neighbor matching in low-dimensional PCA space outperforms raw pixel matching by suppressing high-frequency noise and minor illumination variations.

Supervised Classification: Supervised models such as Logistic Regression and Support Vector Machines (SVM) trained on compact PCA feature vectors achieve superior recognition accuracy compared to distance-based baselines.
