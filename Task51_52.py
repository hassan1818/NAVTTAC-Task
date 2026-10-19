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
# TASK 51
# =============================================================================
"""
TASK 51: Machine Learning (Implement Linear Regression)
Reference Link: https://stackabuse.com/linear-regression-in-python-with-scikit-learn/

"""
print("=" * 70)
print("TASK 51: Machine Learning - Linear Regression Implementation")
print("=" * 70)

# 1. Dataset: Student Study Hours & Attendance predicting Exam Score
np.random.seed(42)
n_samples = 100
study_hours = np.random.uniform(1.0, 10.0, n_samples)
attendance_rate = np.random.uniform(60.0, 100.0, n_samples)
# True relationship: score = 15 + 5.5 * study_hours + 0.3 * attendance + noise
exam_score = 15 + (5.5 * study_hours) + (0.3 * attendance_rate) + np.random.normal(0, 2.5, n_samples)

X_lr = np.column_stack([study_hours, attendance_rate])
y_lr = exam_score

# 2. Train-test split
X_train_lr, X_test_lr, y_train_lr, y_test_lr = train_test_split(X_lr, y_lr, test_size=0.2, random_state=42)

# 3. Model training
lr_model = LinearRegression()
lr_model.fit(X_train_lr, y_train_lr)

# 4. Coefficients
print(f"Intercept (b0)          : {lr_model.intercept_:.4f}")
print(f"Coefficients [Hours, Att]: {lr_model.coef_.round(4)}")

# 5. Prediction and Evaluation
y_pred_lr = lr_model.predict(X_test_lr)
mae = mean_absolute_error(y_test_lr, y_pred_lr)
mse = mean_squared_error(y_test_lr, y_pred_lr)
rmse = np.sqrt(mse)
r2 = r2_score(y_test_lr, y_pred_lr)

print("\nModel Evaluation Metrics on Test Set:")
print(f"   Mean Absolute Error (MAE) : {mae:.4f}")
print(f"   Mean Squared Error (MSE)  : {mse:.4f}")
print(f"   Root Mean Squared (RMSE)  : {rmse:.4f}")
print(f"   R-squared (R2 Score)      : {r2:.4f} (Explains {r2*100:.1f}% variance)")


# =============================================================================
# TASK 52
# =============================================================================
"""
TASK 52: Machine Learning (Perform Logistic Regression)
Reference Links:
- https://towardsdatascience.com/logistic-regression-using-python-sklearn-numpy-mnist-handwriting-recognition-matplotlib-a6b31e2b166a
- https://www.datacamp.com/community/tutorials/understanding-logistic-regression-python

"""
print("\n" + "=" * 70)
print("TASK 52: Machine Learning - Logistic Regression Implementation")
print("=" * 70)

# 1. Load Breast Cancer classification dataset
cancer = load_breast_cancer()
X_cancer = cancer.data[:, :6]  # Use first 6 key morphological features
y_cancer = cancer.target        # 0 = Malignant, 1 = Benign

X_train_log, X_test_log, y_train_log, y_test_log = train_test_split(
    X_cancer, y_cancer, test_size=0.25, random_state=42, stratify=y_cancer
)

# 2. Scaling
scaler = StandardScaler()
X_train_log = scaler.fit_transform(X_train_log)
X_test_log = scaler.transform(X_test_log)

# 3. Fit Logistic Regression
log_reg = LogisticRegression(random_state=42)
log_reg.fit(X_train_log, y_train_log)

# 4. Predictions
y_pred_log = log_reg.predict(X_test_log)
acc_log = accuracy_score(y_test_log, y_pred_log)

print(f"Logistic Regression Accuracy: {acc_log * 100:.2f}%\n")
print("Confusion Matrix:")
print(confusion_matrix(y_test_log, y_pred_log))

print("\nClassification Report:")
print(classification_report(y_test_log, y_pred_log, target_names=cancer.target_names))