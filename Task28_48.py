
# =============================================================================
# TASK 28
# =============================================================================
"""
TASK 28: NumPy (Exercise on NumPy Array Creation)
Reference Link: https://www.w3schools.com/python/numpy_creating_arrays.asp

"""
print("\n" + "=" * 70)
print("TASK 28: NumPy - Array Creation Exercises")
print("=" * 70)

# 1. Multi-dimensional Arrays
arr_0d = np.array(42)
arr_1d = np.array([1, 2, 3, 4, 5])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print(f"0-D Array: {arr_0d} | ndim: {arr_0d.ndim}")
print(f"1-D Array: {arr_1d} | ndim: {arr_1d.ndim}")
print(f"2-D Array:\n{arr_2d}\n   ndim: {arr_2d.ndim}")
print(f"3-D Array:\n{arr_3d}\n   ndim: {arr_3d.ndim}")

# 2. Built-in creators
zeros_arr = np.zeros((2, 3))
ones_arr = np.ones((2, 2))
range_arr = np.arange(10, 25, 3)
linspace_arr = np.linspace(0, 1, 5)

print(f"\nnp.zeros((2, 3)):\n{zeros_arr}")
print(f"np.ones((2, 2)):\n{ones_arr}")
print(f"np.arange(10, 25, 3): {range_arr}")
print(f"np.linspace(0, 1, 5): {linspace_arr}")


# =============================================================================
# TASK 29
# =============================================================================
"""
TASK 29: NumPy (Exercise on NumPy Array Indexing)
Reference Link: https://www.w3schools.com/python/numpy_array_indexing.asp

"""
print("\n" + "=" * 70)
print("TASK 29: NumPy - Array Indexing Exercises")
print("=" * 70)

# 1. 1D Indexing
arr_1d = np.array([10, 20, 30, 40, 50])
print(f"1D Array: {arr_1d}")
print(f"Element at index 0 : {arr_1d[0]}")
print(f"Element at index 3 : {arr_1d[3]}")
print(f"Element at index -1: {arr_1d[-1]}")

# 2. 2D Indexing
arr_2d = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(f"\n2D Array:\n{arr_2d}")
print(f"Element at row 0, col 1 [0, 1] : {arr_2d[0, 1]}")
print(f"Element at row 2, col 2 [2, 2] : {arr_2d[2, 2]}")
print(f"Last row, last column [-1, -1] : {arr_2d[-1, -1]}")


# =============================================================================
# TASK 30
# =============================================================================
"""
TASK 30: NumPy (Exercise on NumPy Array Slicing)
Reference Link: https://www.w3schools.com/python/numpy_array_slicing.asp

"""
print("\n" + "=" * 70)
print("TASK 30: NumPy - Array Slicing Exercises")
print("=" * 70)

# 1. 1D Slicing
arr_1d = np.array([10, 20, 30, 40, 50, 60, 70, 80])
print(f"Original 1D Array: {arr_1d}")
print(f"Slice from index 2 to 6 [2:6]     : {arr_1d[2:6]}")
print(f"Slice from index 3 to end [3:]     : {arr_1d[3:]}")
print(f"Slice from beginning to 4 [:4]     : {arr_1d[:4]}")
print(f"Slice with step 2 [1:7:2]          : {arr_1d[1:7:2]}")

# 2. 2D Slicing
arr_2d = np.array([
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12]
])
print(f"\nOriginal 2D Matrix (3x4):\n{arr_2d}")
print(f"Extract rows 0 to 1, column 2 arr[0:2, 2]:\n{arr_2d[0:2, 2]}")
print(f"Extract 2x2 top-right sub-matrix arr[0:2, 2:4]:\n{arr_2d[0:2, 2:4]}")
print(f"Extract all rows, alternating columns arr[:, ::2]:\n{arr_2d[:, ::2]}")
print("=" * 70)


import numpy as np

# =============================================================================
# TASK 31
# =============================================================================
"""
TASK 31: NumPy (Exercise on NumPy Data Types)
Reference Link: https://www.w3schools.com/python/numpy_data_types.asp

"""
print("=" * 70)
print("TASK 31: NumPy - Data Types Exercises")
print("=" * 70)

# 1. Checking data types
int_arr = np.array([1, 2, 3, 4])
str_arr = np.array(["Python", "NumPy", "Pandas"])
print(f"int_arr dtype        : {int_arr.dtype}")
print(f"str_arr dtype        : {str_arr.dtype}")

# 2. Creating with specified types
arr_f4 = np.array([1.2, 3.4, 5.6], dtype='f4')
print(f"arr_f4 (float32)     : {arr_f4} | dtype: {arr_f4.dtype}")

# 3. Converting data types using astype
float_values = np.array([1.1, 2.7, 3.9, 4.2])
converted_int = float_values.astype('i')
converted_bool = np.array([1, 0, 3, 0]).astype(bool)

print(f"Original floats      : {float_values}")
print(f"Converted to int (i) : {converted_int} | dtype: {converted_int.dtype}")
print(f"Converted to bool    : {converted_bool} | dtype: {converted_bool.dtype}")


# =============================================================================
# TASK 32
# =============================================================================
"""
TASK 32: NumPy (Exercise on NumPy Array Copy vs View)
Reference Link: https://www.w3schools.com/python/numpy_copy_vs_view.asp

"""
print("\n" + "=" * 70)
print("TASK 32: NumPy - Copy vs View Exercises")
print("=" * 70)

original = np.array([10, 20, 30, 40, 50])

# Create copy and view
arr_copy = original.copy()
arr_view = original.view()

# Modify original array
original[0] = 999

print(f"Original after change arr[0]=999 : {original}")
print(f"arr_copy (not affected by change): {arr_copy}")
print(f"arr_view (affected by change)    : {arr_view}")

# Checking ownership using .base
print(f"arr_copy.base (owns data -> None): {arr_copy.base}")
print(f"arr_view.base (references data)  : {arr_view.base is original}")


# =============================================================================
# TASK 33
# =============================================================================
"""
TASK 33: NumPy (Exercise on NumPy Array Shape)
Reference Link: https://www.w3schools.com/python/numpy_array_shape.asp

"""
print("\n" + "=" * 70)
print("TASK 33: NumPy - Array Shape Exercises")
print("=" * 70)

arr_1d = np.array([1, 2, 3, 4, 5])
arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])

print(f"1D Array Shape (5 elements)     : {arr_1d.shape}")
print(f"2D Array Shape (2 rows, 4 cols) : {arr_2d.shape}")
print(f"3D Array Shape (3x2x2)          : {arr_3d.shape}")

# Using ndmin to enforce 5 dimensions
arr_5d = np.array([1, 2, 3, 4], ndmin=5)
print(f"Array created with ndmin=5 shape: {arr_5d.shape}")


# =============================================================================
# TASK 34
# =============================================================================
"""
TASK 34: NumPy (Exercise on NumPy Array Reshaping)
Reference Link: https://www.w3schools.com/python/numpy_array_reshape.asp

"""
print("\n" + "=" * 70)
print("TASK 34: NumPy - Array Reshaping Exercises")
print("=" * 70)

data = np.arange(1, 13)
print(f"Original 1D array (12 elements):\n{data}")

# 1. Reshape to 2D (4 rows, 3 columns)
arr_4x3 = data.reshape(4, 3)
print(f"\nReshaped to 4x3:\n{arr_4x3}")

# 2. Reshape to 3D (2x3x2)
arr_2x3x2 = data.reshape(2, 3, 2)
print(f"\nReshaped to 3D (2x3x2):\n{arr_2x3x2}")

# 3. Unknown dimension with -1
arr_unknown = data.reshape(2, -1)
print(f"\nReshaped using (2, -1) [automatically computes 6 cols]:\n{arr_unknown.shape}")

# 4. Flattening back to 1D
flattened = arr_4x3.reshape(-1)
print(f"\nFlattened back to 1D:\n{flattened}")


# =============================================================================
# TASK 35
# =============================================================================
"""
TASK 35: NumPy (Exercise on NumPy Array Iterating)
Reference Link: https://www.w3schools.com/python/numpy_array_iterating.asp

"""
print("\n" + "=" * 70)
print("TASK 35: NumPy - Array Iterating Exercises")
print("=" * 70)

matrix = np.array([[10, 20, 30], [40, 50, 60]])

# 1. Standard row iteration
print("1. Standard iteration over 2D array (by rows):")
for row in matrix:
    print(f"   Row: {row}")

# 2. Using np.nditer() for element-by-element traversal
print("\n2. Element-by-element traversal with np.nditer():")
for val in np.nditer(matrix):
    print(f"{val}", end=" ")
print()

# 3. Iterating with step using slicing inside nditer
print("\n3. Iterating with step 2 across all columns [:, ::2]:")
for val in np.nditer(matrix[:, ::2]):
    print(f"{val}", end=" ")
print()


# =============================================================================
# TASK 36
# =============================================================================
"""
TASK 36: NumPy (Exercise on NumPy Matrix / Array Joining)
Reference Link: https://www.w3schools.com/python/numpy_array_join.asp

"""
print("\n" + "=" * 70)
print("TASK 36: NumPy - Matrix / Array Joining Exercises")
print("=" * 70)

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# 1. Concatenation
cat_axis0 = np.concatenate((a, b), axis=0)  # vertical stacking
cat_axis1 = np.concatenate((a, b), axis=1)  # horizontal stacking

print(f"Matrix A:\n{a}")
print(f"Matrix B:\n{b}")
print(f"\nConcatenate along axis=0 (rows):\n{cat_axis0}")
print(f"\nConcatenate along axis=1 (columns):\n{cat_axis1}")

# 2. Stacking functions
hstack_result = np.hstack((a, b))
vstack_result = np.vstack((a, b))
dstack_result = np.dstack((a, b))

print(f"\nnp.hstack (stack along rows):\n{hstack_result}")
print(f"\nnp.vstack (stack along cols):\n{vstack_result}")
print(f"\nnp.dstack (stack along depth) shape: {dstack_result.shape}")


# =============================================================================
# TASK 37
# =============================================================================
"""
TASK 37: NumPy (Exercise on NumPy Array Splitting)
Reference Link: https://www.w3schools.com/python/numpy_array_split.asp

"""
print("\n" + "=" * 70)
print("TASK 37: NumPy - Array Splitting Exercises")
print("=" * 70)

# 1. 1D Array Splitting
arr_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8])
splits_1d = np.array_split(arr_1d, 3)
print(f"Original 1D array: {arr_1d}")
print("Split into 3 sub-arrays:")
for idx, part in enumerate(splits_1d, 1):
    print(f"   Part {idx}: {part}")

# 2. 2D Array Splitting
arr_2d = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160]
])
print(f"\nOriginal 2D Array (4x4):\n{arr_2d}")

v_splits = np.vsplit(arr_2d, 2)
print(f"\nnp.vsplit into 2 parts (top 2 rows, bottom 2 rows):")
print(f"Upper half:\n{v_splits[0]}")
print(f"Lower half:\n{v_splits[1]}")

h_splits = np.hsplit(arr_2d, 2)
print(f"\nnp.hsplit into 2 parts (left 2 cols, right 2 cols):")
print(f"Left half:\n{h_splits[0]}")
print(f"Right half:\n{h_splits[1]}")


# =============================================================================
# TASK 38
# =============================================================================
"""
TASK 38: NumPy (Exercise on NumPy Array Searching)
Reference Link: https://www.w3schools.com/python/numpy_array_search.asp

"""
print("\n" + "=" * 70)
print("TASK 38: NumPy - Array Searching Exercises")
print("=" * 70)

arr = np.array([10, 25, 40, 25, 50, 25, 80])
print(f"Array: {arr}")

# 1. Search with np.where()
indices_25 = np.where(arr == 25)
print(f"Indices where element == 25: {indices_25[0]}")

# 2. Find even indices
even_indices = np.where(arr % 2 == 0)
print(f"Indices of even numbers    : {even_indices[0]} (Values: {arr[even_indices]})")

# 3. searchsorted on sorted array
sorted_arr = np.array([10, 20, 30, 40, 50])
insert_pos = np.searchsorted(sorted_arr, 35)
print(f"Sorted array: {sorted_arr}")
print(f"Index to insert 35 to maintain sort order: {insert_pos}")


# =============================================================================
# TASK 39
# =============================================================================
"""
TASK 39: NumPy (Exercise on NumPy Array Sorting)
Reference Link: https://www.w3schools.com/python/numpy_array_sort.asp

"""
print("\n" + "=" * 70)
print("TASK 39: NumPy - Array Sorting Exercises")
print("=" * 70)

# 1. Numeric sorting
nums = np.array([45, 12, 89, 3, 27, 61])
print(f"Unsorted numeric array : {nums}")
print(f"Sorted numeric array   : {np.sort(nums)}")

# 2. String & Boolean sorting
words = np.array(["Python", "Anaconda", "TensorFlow", "Keras"])
bools = np.array([True, False, True, False])
print(f"\nSorted string array    : {np.sort(words)}")
print(f"Sorted boolean array   : {np.sort(bools)}")

# 3. 2D Array Sorting
grid = np.array([[5, 1, 9], [8, 2, 4]])
print(f"\nOriginal 2D grid:\n{grid}")
print(f"Sorted along axis=1 (within each row):\n{np.sort(grid, axis=1)}")
print(f"Sorted along axis=0 (within each col):\n{np.sort(grid, axis=0)}")


# =============================================================================
# TASK 40
# =============================================================================
"""
TASK 40: NumPy (Exercise on NumPy Array Random Technique)
Reference Link: https://www.w3schools.com/python/numpy_random.asp

"""
print("\n" + "=" * 70)
print("TASK 40: NumPy - Array Random Techniques")
print("=" * 70)

# Seed for reproducible demonstration
np.random.seed(42)

# 1. Random integers
rand_ints = np.random.randint(10, 100, size=(2, 4))
print(f"1. Random 2x4 integer matrix (range 10 to 100):\n{rand_ints}")

# 2. Random floats [0, 1)
rand_floats = np.random.rand(4)
print(f"\n2. Random 1D float array (4 samples):\n{rand_floats}")

# 3. Random choice with probability distribution
options = ["Pass", "Fail", "Distinction"]
probabilities = [0.70, 0.10, 0.20]
sample_results = np.random.choice(options, p=probabilities, size=8)
print(f"\n3. 8 Random choices from {options} with probabilities {probabilities}:")
print(f"   Results: {sample_results}")

# 4. Permutation (shuffle without in-place mutation)
original_sequence = np.arange(1, 9)
shuffled_sequence = np.random.permutation(original_sequence)
print(f"\n4. Original sequence : {original_sequence}")
print(f"   Shuffled sequence : {shuffled_sequence}")
print("=" * 70)

import io
import statistics
import numpy as np
import pandas as pd
from scipy import stats

# =============================================================================
# TASK 41
# =============================================================================
"""
TASK 41: Pandas (Exercise on Pandas Basics / Tutorial)
Reference Link: https://www.w3schools.com/python/pandas_tutorial.asp

"""
print("=" * 70)
print("TASK 41: Pandas - Basics Tutorial Exercises")
print("=" * 70)

# Sample dataset
dataset = {
    'Student': ['Ali', 'Ayesha', 'Bilal', 'Fatima', 'Usman'],
    'Course': ['AI', 'Data Science', 'AI', 'Machine Learning', 'AI'],
    'Score': [92, 85, 78, 96, 88]
}

df_basic = pd.DataFrame(dataset)
print("Basic Pandas DataFrame:")
print(df_basic)
print(f"\nDataFrame Dimensions: {df_basic.shape[0]} rows x {df_basic.shape[1]} columns")


# =============================================================================
# TASK 42
# =============================================================================
"""
TASK 42: Pandas (Exercise on Pandas Getting Started & Installation)
Reference Link: https://www.w3schools.com/python/pandas_getting_started.asp

"""
print("\n" + "=" * 70)
print("TASK 42: Pandas - Installation & Getting Started")
print("=" * 70)

print(f"Pandas Version: {pd.__version__}")

# Simple car dataset
cars_data = {
    'cars': ["Toyota Corolla", "Honda Civic", "Suzuki Swift"],
    'passings': [3, 7, 2]
}
cars_df = pd.DataFrame(cars_data)
print("\nFirst Test DataFrame:")
print(cars_df)


# =============================================================================
# TASK 43
# =============================================================================
"""
TASK 43: Pandas (Exercise on Pandas Series Data)
Reference Link: https://www.w3schools.com/python/pandas_series.asp

"""
print("\n" + "=" * 70)
print("TASK 43: Pandas - Series Data Exercises")
print("=" * 70)

# 1. Series from list with default numeric index
temperatures = [31.5, 33.2, 30.0, 29.8]
s_default = pd.Series(temperatures)
print("1. Series with default index:")
print(s_default)

# 2. Series with custom labels
s_labeled = pd.Series(temperatures, index=["Day 1", "Day 2", "Day 3", "Day 4"])
print("\n2. Series with custom index labels:")
print(s_labeled)
print(f"   Value at 'Day 2': {s_labeled['Day 2']} °C")

# 3. Series from dictionary
calories_dict = {"Mon": 2100, "Tue": 1950, "Wed": 2200}
s_dict = pd.Series(calories_dict)
print("\n3. Series created from Dictionary:")
print(s_dict)


# =============================================================================
# TASK 44
# =============================================================================
"""
TASK 44: Pandas (Exercise on Pandas Data Frame)
Reference Link: https://www.w3schools.com/python/pandas_dataframes.asp

"""
print("\n" + "=" * 70)
print("TASK 44: Pandas - DataFrame Exercises")
print("=" * 70)

workout_data = {
    "calories": [420, 380, 390],
    "duration_mins": [50, 40, 45]
}

# 1. Standard index DataFrame
df_workout = pd.DataFrame(workout_data)
print("1. Workout DataFrame:")
print(df_workout)

# 2. Locating rows using .loc
print(f"\n2. Row at index 0 (Series):\n{df_workout.loc[0]}")
print(f"\n   Rows at index 0 and 1 (DataFrame):\n{df_workout.loc[[0, 1]]}")

# 3. Named index DataFrame
df_named = pd.DataFrame(workout_data, index=["day1", "day2", "day3"])
print(f"\n3. DataFrame with Named Indexes:\n{df_named}")
print(f"\n   Selecting 'day2':\n{df_named.loc['day2']}")


# =============================================================================
# TASK 45
# =============================================================================
"""
TASK 45: Pandas (Exercise on Pandas Open CSV Files)
Reference Link: https://www.w3schools.com/python/pandas_csv.asp

"""
print("\n" + "=" * 70)
print("TASK 45: Pandas - CSV File Ingestion Exercises")
print("=" * 70)

# Self-contained CSV simulation using io.StringIO
csv_buffer = io.StringIO("""Duration,Pulse,Maxpulse,Calories
60,110,130,409.1
60,117,145,479.0
60,103,135,340.0
45,109,175,282.4
45,117,148,406.0
60,102,127,300.0
""")

df_csv = pd.read_csv(csv_buffer)
print("DataFrame loaded from CSV stream:")
print(df_csv.to_string())

print(f"\nCurrent Pandas pd.options.display.max_rows = {pd.options.display.max_rows}")


# =============================================================================
# TASK 46
# =============================================================================
"""
TASK 46: Pandas (Exercise on Pandas Data Analyzing)
Reference Link: https://www.w3schools.com/python/pandas_analyzing.asp

"""
print("\n" + "=" * 70)
print("TASK 46: Pandas - Data Analyzing Exercises")
print("=" * 70)

# Creating representative dataset
np.random.seed(42)
records = {
    'Age': np.random.randint(18, 50, size=15),
    'Experience_Years': np.random.randint(1, 20, size=15),
    'Salary_k': np.random.randint(45, 180, size=15)
}
df_analysis = pd.DataFrame(records)

print("1. First 4 rows (head):")
print(df_analysis.head(4))

print("\n2. Last 3 rows (tail):")
print(df_analysis.tail(3))

print("\n3. Data Structure & Types (info):")
df_analysis.info()

print("\n4. Descriptive Statistics (describe):")
print(df_analysis.describe())


# =============================================================================
# TASK 47
# =============================================================================
"""
TASK 47: Pandas (Exercise on Pandas Data Cleaning Techniques)
Reference Link: https://www.w3schools.com/python/pandas_cleaning.asp

"""
print("\n" + "=" * 70)
print("TASK 47: Pandas - Data Cleaning Exercises")
print("=" * 70)

# Dirty dataset with nulls, format issues, and duplicates
dirty_data = {
    'Date': ['2026-10-01', '2026-10-02', '20261003', '2026-10-04', '2026-10-04'],
    'Duration': [60, 60, 450, 45, 45],  # 450 is a typo for 45
    'Pulse': [110, np.nan, 103, 109, 109],  # NaN value
    'Calories': [409.1, 479.0, 340.0, 282.4, 282.4]  # duplicate row
}
df_dirty = pd.DataFrame(dirty_data)
print("Raw Dirty Dataset:")
print(df_dirty)

# 1. Fill missing values with median
median_pulse = df_dirty['Pulse'].median()
df_dirty['Pulse'] = df_dirty['Pulse'].fillna(median_pulse)

# 2. Fix date formats
df_dirty['Date'] = pd.to_datetime(df_dirty['Date'], format='mixed')

# 3. Fix wrong value (Duration > 120 replaced with 45)
df_dirty.loc[df_dirty['Duration'] > 120, 'Duration'] = 45

# 4. Remove duplicate rows
df_cleaned = df_dirty.drop_duplicates()

print("\nCleaned Dataset:")
print(df_cleaned)


# =============================================================================
# TASK 48
# =============================================================================
"""
TASK 48: Pandas (Exercise on Pandas Data Correlation)
Reference Link: https://www.w3schools.com/python/pandas_correlations.asp

"""
print("\n" + "=" * 70)
print("TASK 48: Pandas - Correlation Exercises")
print("=" * 70)

study_data = {
    'Hours_Studied': [2, 3, 5, 7, 8, 10, 12],
    'Practice_Tests': [1, 2, 3, 4, 5, 7, 8],
    'Exam_Score': [55, 62, 70, 81, 85, 93, 98],
    'TV_Hours': [5, 4, 3, 2, 2, 1, 0]
}
df_study = pd.DataFrame(study_data)
corr_matrix = df_study.corr()

print("Study & Exam Performance Correlation Matrix:")
print(corr_matrix.round(3))

print("\nInterpretation:")
print(f"- Hours_Studied vs Exam_Score : {corr_matrix.loc['Hours_Studied', 'Exam_Score']:.2f} (Strong Positive)")
print(f"- TV_Hours vs Exam_Score      : {corr_matrix.loc['TV_Hours', 'Exam_Score']:.2f} (Strong Negative)")