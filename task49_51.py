# =============================================================================
# TASK 49
# =============================================================================
"""
TASK 49: Stats (Perform Mean, Median, and Mode)
Reference Link: https://www.w3schools.com/python/python_ml_mean_median_mode.asp

"""
print("\n" + "=" * 70)
print("TASK 49: Statistics - Mean, Median, and Mode")
print("=" * 70)

speed_records = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
print(f"Dataset: {speed_records}")

# Mean
mean_val = np.mean(speed_records)
# Median
median_val = np.median(speed_records)
# Mode using statistics module
mode_val = statistics.mode(speed_records)
# Mode using scipy
scipy_mode = stats.mode(speed_records, keepdims=True)

print(f"Mean (Average)           : {mean_val:.2f}")
print(f"Median (Middle value)    : {median_val}")
print(f"Mode (Most common value) : {mode_val} (scipy count: {scipy_mode.count[0]})")


# =============================================================================
# TASK 50
# =============================================================================
"""
TASK 50: Stats (Perform Standard Deviation & Variance)
Reference Link: https://www.w3schools.com/python/python_ml_standard_deviation.asp

"""
print("\n" + "=" * 70)
print("TASK 50: Statistics - Standard Deviation and Variance")
print("=" * 70)

# Dataset A: Consistent speeds
speeds_A = [86, 87, 88, 86, 87, 85, 86]
# Dataset B: Wide dispersion
speeds_B = [32, 111, 138, 28, 59, 77, 97]

std_A = np.std(speeds_A)
var_A = np.var(speeds_A)

std_B = np.std(speeds_B)
var_B = np.var(speeds_B)

print(f"Dataset A: {speeds_A}")
print(f"   Mean: {np.mean(speeds_A):.2f} | Variance: {var_A:.2f} | Standard Deviation: {std_A:.2f}")

print(f"\nDataset B: {speeds_B}")
print(f"   Mean: {np.mean(speeds_B):.2f} | Variance: {var_B:.2f} | Standard Deviation: {std_B:.2f}")

print("\nInsight: Low standard deviation indicates data points cluster close to the mean;")
print("high standard deviation indicates values are dispersed across a wider range.")
print("=" * 70)

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