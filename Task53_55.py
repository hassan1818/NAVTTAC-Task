
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
    accuracy_score,
    confusion_matrix,
    classification_report
)
from sklearn.datasets import load_iris, load_breast_cancer

# =============================================================================
# TASK 53
# =============================================================================
"""
TASK 53: Machine Learning (Exercise on Decision Tree)
Reference Link: https://www.datacamp.com/community/tutorials/decision-tree-classification-python

"""
print("\n" + "=" * 70)
print("TASK 53: Machine Learning - Decision Tree Classification")
print("=" * 70)

iris = load_iris()
X_dt, y_dt = iris.data, iris.target

X_train_dt, X_test_dt, y_train_dt, y_test_dt = train_test_split(
    X_dt, y_dt, test_size=0.2, random_state=42, stratify=y_dt
)

# Train Decision Tree with max_depth=3 to prevent overfitting
dt_classifier = DecisionTreeClassifier(criterion="gini", max_depth=3, random_state=42)
dt_classifier.fit(X_train_dt, y_train_dt)

y_pred_dt = dt_classifier.predict(X_test_dt)
acc_dt = accuracy_score(y_test_dt, y_pred_dt)

print(f"Decision Tree Accuracy on Iris Test Set: {acc_dt * 100:.2f}%\n")

# Feature importances
print("Feature Importances:")
for name, imp in zip(iris.feature_names, dt_classifier.feature_importances_):
    print(f"   {name:<25}: {imp:.4f}")

# Tree Decision Rules
print("\nDecision Tree Structure / Text Rules:")
tree_rules = export_text(dt_classifier, feature_names=list(iris.feature_names))
print(tree_rules)


# =============================================================================
# TASK 54
# =============================================================================
"""
TASK 54: Machine Learning (Exercise on SVM - Support Vector Machine)
Reference Link: https://stackabuse.com/implementing-svm-and-kernel-svm-with-pythons-scikit-learn/

"""
print("\n" + "=" * 70)
print("TASK 54: Machine Learning - Support Vector Machine (SVM)")
print("=" * 70)

# Using Iris dataset for kernel comparison
svm_linear = SVC(kernel='linear', C=1.0, random_state=42)
svm_linear.fit(X_train_dt, y_train_dt)
pred_linear = svm_linear.predict(X_test_dt)
acc_linear = accuracy_score(y_test_dt, pred_linear)

svm_rbf = SVC(kernel='rbf', C=1.0, gamma='scale', random_state=42)
svm_rbf.fit(X_train_dt, y_train_dt)
pred_rbf = svm_rbf.predict(X_test_dt)
acc_rbf = accuracy_score(y_test_dt, pred_rbf)

print(f"1. SVM with Linear Kernel Accuracy : {acc_linear * 100:.2f}%")
print(f"2. SVM with RBF (Kernel) Accuracy  : {acc_rbf * 100:.2f}%")
print("\nConclusion: Non-linear RBF kernel maps features into higher dimensions")
print("to effectively separate complex boundaries, while Linear kernel is optimal for linearly separable data.")


# =============================================================================
# TASK 55
# =============================================================================
"""
TASK 55: Machine Learning (Exercise on Time Series Analysis)
Reference Link: https://www.dataquest.io/blog/tutorial-time-series-analysis-with-pandas

"""
print("\n" + "=" * 70)
print("TASK 55: Machine Learning - Time Series Analysis with Pandas")
print("=" * 70)

# 1. Generate 90 days of daily time-series data
dates = pd.date_range(start="2026-01-01", periods=90, freq="D")
np.random.seed(42)

# Trend + 7-day Weekly Seasonality + Random Noise
trend = np.linspace(100, 160, 90)
seasonality = 15 * np.sin(2 * np.pi * np.arange(90) / 7)
noise = np.random.normal(0, 3, 90)
consumption = trend + seasonality + noise

ts_df = pd.DataFrame({'Consumption_kWh': consumption}, index=dates)

# 2. Resample: Weekly Average
weekly_summary = ts_df.resample('W').mean()

# 3. Rolling 7-day average
ts_df['7_Day_Moving_Avg'] = ts_df['Consumption_kWh'].rolling(window=7).mean()

# 4. Lag feature (Yesterday's consumption)
ts_df['Lag_1_Day'] = ts_df['Consumption_kWh'].shift(1)

print("Time Series Data Snapshot (first 10 days with Moving Average & Lag):")
print(ts_df.head(10).round(2))

print("\nWeekly Resampled Average (First 4 weeks):")
print(weekly_summary.head(4).round(2))
