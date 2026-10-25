MSc DS DS605: Fundamentals of Machine Learning  

Lab Assignment - 8

Student Id: 202618017

Decision Trees and Support Vector Machines

This project implements Decision Tree and Linear Soft-Margin SVM classifiers from scratch using NumPy and Pandas, benchmarking them against Scikit-Learn implementations on the UCI Banknote Authentication dataset and synthetic non-linear data (make_moons). The custom implementations closely mirror library outputs, with the manual Decision Tree matching Scikit-Learn's performance exactly (93.09% accuracy, 0.9261 F1-score) and the manual Linear SVM achieving comparable precision to Scikit-Learn's linear model (88.00% vs 87.64% accuracy). Across all models, Decision Trees demonstrated high performance and fast inference times, while subgradient descent for the manual linear SVM successfully converged across training epochs.
