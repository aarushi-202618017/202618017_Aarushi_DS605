# Live Deployed Link: https://202618017mllab04airbnb.streamlit.app/
# NYC Airbnb Nightly Price Predictor

An end-to-end Machine Learning solution that predicts nightly Airbnb listing prices across New York City. Built as part of **DS605: Fundamentals of Machine Learning**, this project covers data cleaning, feature engineering, model selection, hyperparameter tuning, and interactive deployment.

---

## Project Architecture & Workflow

1. **Data Preprocessing & Cleaning**:
   * Removed extreme price outliers ($> \$500$) and unrealistic minimum stay limits ($> 365$ nights).
   * Handled missing value distributions (e.g., filled missing `reviews_per_month` with `0`).
   * Applied target log-transformation (`np.log1p`) to stabilize right-skewed price variance.

2. **Feature Engineering**:
   * **`dist_to_midtown`**: Calculated spatial Euclidean distance from listing coordinates to Midtown Manhattan ($40.7580, -73.9855$).
   * Standardized numerical features via `StandardScaler` and encoded categorical attributes (`neighbourhood_group`, `room_type`) using `OneHotEncoder`.

3. **Model Selection & Tuning**:
   * Evaluated Multiple Regressors: Linear Regression, Ridge Regression, Decision Tree, and Random Forest.
   * **Selected Model**: `RandomForestRegressor` tuned via `RandomizedSearchCV`.
   * **Final Performance**:
     * **Test $R^2$**: `0.5219`
     * **Test RMSE**: `\$61.74`
     * **Test MAE**: `\$38.50`

---

## Artifact Generation & Repository Setup

The primary execution environment for this project is the Google Colab notebook (`notebooks/airbnb_price_prediction.ipynb`). 

* **Automated Export**: Running the notebook end-to-end programmatically builds the Scikit-Learn pipeline, exports the trained model artifact (`airbnb_model.pkl`), and writes the application code (`app.py`) using `%%writefile`.
* **Repository Safety**: Although these files are programmatically compiled during runtime, `app.py` and `airbnb_model.pkl` are explicitly tracked and committed directly to this GitHub repository to ensure immediate availability for automated deployment pipelines.

---

##  Repository Structure

```text
├── airbnb_price_prediction.ipynb   # Complete analysis, training, and tuning notebook
├── airbnb_model.pkl                    # Saved Scikit-Learn model pipeline
├── app.py                              # Streamlit web application script
├── requirements.txt                    # Project dependencies for deployment
└── README.md                           # Documentation
