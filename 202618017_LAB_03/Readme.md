202618017

Lab 03 DS605

Fundamentals of Machine Learning

In this colab notebooka and lab session, we built an end-to-end machine learning workflow to predict hotel booking cancellations, starting with data cleaning that involved dropping high-missingness or leakage columns (like company and reservation_status) and removing extreme numerical outliers using the IQR method. We then constructed dynamic preprocessing pipelines using ColumnTransformer to handle missing values with KNNImputer and SimpleImputer, encode categorical variables, and apply different scaling techniques (StandardScaler and MinMaxScaler). Finally, we trained four model combinations using Logistic Regression and Decision Trees, evaluated their performance using metrics like accuracy and F1-score, and visualized the results with confusion matrices. Through this process, we practically demonstrated key data science concepts, such as identifying severe overfitting in unpruned Decision Trees, recognizing the stability of Logistic Regression, and proving that tree-based algorithms are entirely unaffected by feature scaling.
