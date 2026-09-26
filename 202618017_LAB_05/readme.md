**DS605 FUNDAMENTALS OF MACHINE LEARNING MSc DS** 

**Student Id: 202618017**

Student Name: Aarushi Rana

**Lab 05 Description:**

The notebook compares `scikit-learn` and custom (from-scratch) implementations of Linear and Logistic Regression for predicting garment worker productivity.

 **Key Observations**

*   **Linear Regression Performance**: Both `scikit-learn` and custom models yielded identical MAE, RMSE, and R² scores, as both solve the same Normal Equation.
*   **Linear Regression Runtime**: The **custom linear regression trained faster** (~0.005s) than `scikit-learn` (~0.024s), due to reduced overhead from direct NumPy operations.
*   **Logistic Regression Performance**: The **custom model showed slightly higher accuracy and F1-score** (0.7542 vs 0.7417 Accuracy), likely because the `scikit-learn` version uses default L2 regularization while the custom one does not.
*   **Logistic Regression Runtime**: **`scikit-learn`'s logistic regression trained significantly faster** (~0.016s) than the custom implementation (~0.714s). This is attributed to `scikit-learn`'s highly optimized C-compiled solvers (e.g., L-BFGS) compared to the custom Python Gradient Descent loop.
*   **Prediction Speed**: Both `scikit-learn` and custom models demonstrated **extremely fast prediction times** (under 0.001s), as inference is a simple vectorized matrix multiplication.
