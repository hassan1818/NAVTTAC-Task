
import sys
import os
import cmath

def safe_input(prompt: str, default: str) -> str:
    """Helper function to allow user input if interactive, or use default if non-interactive."""
    try:
        if sys.stdin and sys.stdin.isatty():
            val = input(f"{prompt} (default '{default}'): ").strip()
            return val if val else default
        return default
    except (EOFError, OSError):
        return default


# =============================================================================
# TASK 1
# =============================================================================
"""
TASK 1: Installation
Statement:
Download and install Anaconda3
Install PyTorch
Install TensorFlow 2.0
Install VSCode
Install PyCharm
Week: 1
"""
print("=" * 70)
print("TASK 1: Software & Environment Installation Verification")
print("=" * 70)

def task_1_installation_check():
    print("Verifying installed AI/ML environment and libraries:\n")
    print(f"Python executable : {sys.executable}")
    print(f"Python Version    : {sys.version.split()[0]}")

    # Check PyTorch
    try:
        import torch
        print(f"PyTorch Version   : {torch.__version__} (Installed)")
    except ImportError:
        print("PyTorch           : Not installed. Run: pip install torch torchvision")

    # Check TensorFlow
    try:
        import tensorflow as tf
        print(f"TensorFlow Version: {tf.__version__} (Installed)")
    except ImportError:
        print("TensorFlow        : Not installed. Run: pip install tensorflow")

    # Tools installation guide:
    print("\n[Installation Reference Guide]:")
    print("1. Anaconda3 : Download installer from https://www.anaconda.com/download")
    print("2. VSCode    : Download installer from https://code.visualstudio.com/")
    print("3. PyCharm   : Download Community Edition from https://www.jetbrains.com/pycharm/")
    print("4. PyTorch   : Command -> conda install pytorch torchvision -c pytorch")
    print("5. TensorFlow: Command -> pip install tensorflow")

task_1_installation_check()


# =============================================================================
# TASK 2
# =============================================================================
"""
TASK 2: Linux Commands
Statement:
Practice these commands:
pwd, cd, ls, cat, sudo, man, redirection, mkdir, rm, rmdir, cp, mv, file,
reading, cat, more, less, head, alias, shutdown, restart, touch, nano, bash,
sh, chmod, ps, kill, dpkg
Week: 1
"""
print("\n" + "=" * 70)
print("TASK 2: Linux Commands Simulation & Python Equivalence")
print("=" * 70)

def task_2_linux_commands():
    import shutil
    import subprocess
    from pathlib import Path

    print("Linux Command Reference & Python Equivalents:\n")
    commands_guide = [
        ("pwd", "Print Working Directory", "os.getcwd()", os.getcwd()),
        ("ls", "List Directory Contents", "os.listdir('.')", str(os.listdir('.'))),
        ("mkdir", "Make Directory", "os.makedirs('demo_dir', exist_ok=True)", "Creates a directory"),
        ("touch", "Create empty file / update timestamp", "Path('demo.txt').touch()", "Touches file"),
        ("cat", "Concatenate & display file content", "open('file').read()", "Reads full text"),
        ("head", "Display first N lines of file", "file.readlines()[:10]", "Shows head lines"),
        ("cp", "Copy file or folder", "shutil.copy(src, dst)", "Copies file"),
        ("mv", "Move or rename file", "shutil.move(src, dst)", "Moves/renames file"),
        ("rm", "Remove file", "os.remove(path)", "Deletes file"),
        ("rmdir", "Remove empty directory", "os.rmdir(path)", "Deletes empty dir"),
        ("chmod", "Change file permissions", "os.chmod(path, mode)", "Alters permissions"),
        ("ps", "Show running processes", "subprocess.run(['ps', 'aux'])", "Lists active processes"),
        ("kill", "Terminate process by PID", "os.kill(pid, signal.SIGTERM)", "Terminates process"),
        ("man", "Manual pages", "subprocess.run(['man', cmd])", "Displays command help"),
        ("sudo", "Execute command with superuser privileges", "sudo <command>", "Superuser privilege"),
        ("dpkg", "Debian package manager", "dpkg -i package.deb", "Manages .deb packages")
    ]

    for cmd, purpose, py_equiv, sample in commands_guide[:8]:
        print(f"Command   : {cmd}")
        print(f"Purpose   : {purpose}")
        print(f"Python    : {py_equiv}")
        print(f"Example/Value: {sample}")
        print("-" * 50)

task_2_linux_commands()


# =============================================================================
# TASK 3
# =============================================================================
"""
TASK 3: Python (Add Two Numbers)
"""
print("\n" + "=" * 70)
print("TASK 3: Python - Add Two Predefined Numbers")
print("=" * 70)

# Solution:
num1 = 1.5
num2 = 6.3

# Add two numbers
sum_result = num1 + num2

# Display the sum using format()
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum_result))


# =============================================================================
# TASK 4
# =============================================================================
"""
TASK 4: Python (Add Two Numbers from User Input)
"""
print("\n" + "=" * 70)
print("TASK 4: Python - Add Two Numbers from User Input")
print("=" * 70)

# Solution:
input_val1 = safe_input("Enter first number", "12.4")
input_val2 = safe_input("Enter second number", "7.6")

num1 = float(input_val1)
num2 = float(input_val2)

# Add two numbers
total_sum = num1 + num2

# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, total_sum))


# =============================================================================
# TASK 5
# =============================================================================
"""
TASK 5: Python (Calculate Square Root)
"""
print("\n" + "=" * 70)
print("TASK 5: Python - Calculate the Square Root")
print("=" * 70)

# Solution:
num_input = safe_input("Enter a number to find its square root", "8")
num = float(num_input)

# Exponentiation by 0.5 computes square root
num_sqrt = num ** 0.5
print('The square root of %0.3f is %0.3f' % (num, num_sqrt))


# =============================================================================
# TASK 6
# =============================================================================
"""
TASK 6: Python (Square Root of Real or Complex Numbers)
"""
print("\n" + "=" * 70)
print("TASK 6: Python - Square Root of Real or Complex Numbers")
print("=" * 70)

# Solution:
complex_input_str = safe_input("Enter a complex or real number", "1+2j")
try:
    num_complex = complex(complex_input_str)
except ValueError:
    num_complex = 1 + 2j

# Compute complex square root
num_sqrt_complex = cmath.sqrt(num_complex)
print('The square root of {0} is {1:0.3f}+{2:0.3f}j'.format(
    num_complex, num_sqrt_complex.real, num_sqrt_complex.imag
))


# =============================================================================
# TASK 7
# =============================================================================
"""
TASK 7: Python (Convert Temperature in Celsius to Fahrenheit)
fahrenheit = (celsius * 1.8) + 32
"""
print("\n" + "=" * 70)
print("TASK 7: Python - Convert Celsius to Fahrenheit")
print("=" * 70)

# Solution:
celsius_input = safe_input("Enter temperature in Celsius", "37.5")
celsius = float(celsius_input)

# Temperature conversion formula: F = (C * 1.8) + 32
fahrenheit = (celsius * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' % (celsius, fahrenheit))


# =============================================================================
# TASK 8
# =============================================================================
"""
TASK 8: Python (Find Area of Triangle using Heron's Formula)
Statement:
"""
print("\n" + "=" * 70)
print("TASK 8: Python - Area of Triangle (Heron's Formula)")
print("=" * 70)

# Solution:
side_a = float(safe_input("Enter side a", "5"))
side_b = float(safe_input("Enter side b", "6"))
side_c = float(safe_input("Enter side c", "7"))

# Semi-perimeter calculation
s = (side_a + side_b + side_c) / 2.0

# Heron's formula for area
area = (s * (s - side_a) * (s - side_b) * (s - side_c)) ** 0.5
print('The area of the triangle with sides %0.1f, %0.1f, %0.1f is %0.2f' % (side_a, side_b, side_c, area))


# =============================================================================
# TASK 9
# =============================================================================
"""
TASK 9: Python (Solve Quadratic Equation ax^2 + bx + c = 0)
Statement:
Solve the quadratic equation ax**2 + bx + c = 0
"""
print("\n" + "=" * 70)
print("TASK 9: Python - Solve Quadratic Equation")
print("=" * 70)

# Solution:
qa = float(safe_input("Enter coefficient a", "1"))
qb = float(safe_input("Enter coefficient b", "5"))
qc = float(safe_input("Enter coefficient c", "6"))

# Calculate the discriminant
d = (qb ** 2) - (4 * qa * qc)

# Find two solutions (handles real and complex roots)
sol1 = (-qb - cmath.sqrt(d)) / (2 * qa)
sol2 = (-qb + cmath.sqrt(d)) / (2 * qa)

print(f"Quadratic Equation: ({qa})x^2 + ({qb})x + ({qc}) = 0")
print(f"Discriminant (b^2 - 4ac): {d}")
print('The solutions are {0} and {1}'.format(sol1, sol2))


# =============================================================================
# TASK 10
# =============================================================================
"""
TASK 10: Python (Convert Kilometers to Miles)
"""
print("\n" + "=" * 70)
print("TASK 10: Python - Convert Kilometers to Miles")
print("=" * 70)

# Solution:
km_input = safe_input("Enter value in kilometers", "100")
kilometers = float(km_input)

# Conversion factor: 1 kilometer = 0.621371 miles
conv_fac = 0.621371

# Calculate miles
miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' % (kilometers, miles))
print("=" * 70)


# =============================================================================
# TASK 11
# =============================================================================
"""
TASK 11: Python (Simple 'if' Statement)

"""
print("=" * 70)
print("TASK 11: Python - Simple 'if' Statement Demonstration")
print("=" * 70)

# Solution:
i = 10
if (i > 15):
    print("10 is greater than 15")
print("I am Not in if (Condition i > 15 evaluated to False for i = 10)")


# =============================================================================
# TASK 12
# =============================================================================
"""
TASK 12: Python ('if-else' Statement)

"""
print("\n" + "=" * 70)
print("TASK 12: Python - 'if-else' Conditional Statement")
print("=" * 70)

# Solution:
i = 20
if (i < 15):
    print("i is smaller than 15")
    print("i'm in if Block")
else:
    print("i is greater than 15")
    print("i'm in else Block")
print("i'm not in if and not in else Block")


# =============================================================================
# TASK 13
# =============================================================================
"""
TASK 13: Python (Nested 'if' Statement)

"""
print("\n" + "=" * 70)
print("TASK 13: Python - Nested 'if' Statements")
print("=" * 70)

# Solution:
i = 10
if (i == 10):
    # First if statement
    if (i < 15):
        print("i is smaller than 15")
    # Nested if statement
    if (i < 12):
        print("i is smaller than 12 too")
    else:
        print("i is greater than 15")


# =============================================================================
# TASK 14
# =============================================================================
"""
TASK 14: Python ('if-elif-else' Ladder)

"""
print("\n" + "=" * 70)
print("TASK 14: Python - 'if-elif-else' Ladder")
print("=" * 70)

# Solution:
i = 20
if (i == 10):
    print("i is 10")
elif (i == 15):
    print("i is 15")
elif (i == 20):
    print("i is 20")
else:
    print("i is not present")


# =============================================================================
# TASK 15
# =============================================================================
"""
TASK 15: Python (Exercise on 'for' Loops)
Reference Link: https://www.geeksforgeeks.org/python-for-loops/

"""
print("\n" + "=" * 70)
print("TASK 15: Python - Exercises on 'for' Loops")
print("=" * 70)

# 1. Iterating over list
fruits = ["Apple", "Banana", "Cherry"]
print("1. Iterating through list:")
for fruit in fruits:
    print(f"   Item: {fruit}")

# 2. Using range(start, stop, step)
print("\n2. Using range(2, 11, 2) [Even numbers up to 10]:")
for n in range(2, 11, 2):
    print(f"   {n}", end=" ")
print()

# 3. Nested for loops (Multiplication table snippet)
print("\n3. Nested for loops (2x3 grid):")
for r in range(1, 3):
    for c in range(1, 4):
        print(f"   Cell({r},{c}) = {r*c}", end=" | ")
    print()

# 4. for-else block (executes only if loop completes without break)
print("\n4. for-else construct:")
search_target = 99
numbers = [10, 20, 30, 40]
for num in numbers:
    if num == search_target:
        print(f"   Found {search_target}!")
        break
else:
    print(f"   {search_target} was not found in the list (else block executed).")


# =============================================================================
# TASK 16
# =============================================================================
"""
TASK 16: Python (Exercise on 'while' Loops)
Reference Link: https://www.geeksforgeeks.org/python-while-loops/

"""
print("\n" + "=" * 70)
print("TASK 16: Python - Exercises on 'while' Loops")
print("=" * 70)

# 1. Counter-controlled while loop
print("1. Countdown using while loop:")
count = 5
while count > 0:
    print(f"   Countdown: {count}")
    count -= 1
print("   Blast off!")

# 2. Summation of first N numbers
n = 10
total_sum = 0
curr = 1
while curr <= n:
    total_sum += curr
    curr += 1
print(f"\n2. Sum of first {n} natural numbers is: {total_sum}")

# 3. while-else loop
print("\n3. while-else construct:")
x = 1
while x <= 3:
    print(f"   Loop counter x = {x}")
    x += 1
else:
    print("   while loop condition became False; else block triggered.")


# =============================================================================
# TASK 17
# =============================================================================
"""
TASK 17: Python (Exercise on 'break' Statement)
Reference Link: https://www.geeksforgeeks.org/python-break-statement/

"""
print("\n" + "=" * 70)
print("TASK 17: Python - Exercises on 'break' Statement")
print("=" * 70)

# 1. Break on target element
data = ["AI", "Machine Learning", "Deep Learning", "Robotics", "NLP"]
target = "Deep Learning"
print(f"Searching for '{target}' in list:")
for item in data:
    print(f"   Inspecting: {item}")
    if item == target:
        print(f"   --> Found target '{target}'! Breaking loop now.")
        break

# 2. Infinite loop break
print("\nBreaking out of a while True loop with a threshold:")
counter = 1
while True:
    print(f"   Iteration {counter}")
    if counter >= 3:
        print("   Counter reached 3 -> executing 'break'.")
        break
    counter += 1


# =============================================================================
# TASK 18
# =============================================================================
"""
TASK 18: Python (Exercise on 'continue' Statement)
Reference Link: https://www.geeksforgeeks.org/python-continue-statement/

"""
print("\n" + "=" * 70)
print("TASK 18: Python - Exercises on 'continue' Statement")
print("=" * 70)

# 1. Filter out odd numbers using continue
print("1. Printing only even numbers between 1 and 10:")
for num in range(1, 11):
    if num % 2 != 0:
        continue  # Skip odd numbers
    print(f"   Even number: {num}")

# 2. Skip unwanted characters in string
raw_text = "N-A-V-T-T-C"
clean_text = ""
for char in raw_text:
    if char == "-":
        continue
    clean_text += char
print(f"\n2. Cleaned text (skipping hyphens): '{clean_text}'")


# =============================================================================
# TASK 19
# =============================================================================
"""
TASK 19: Python (Exercise on Various Looping Techniques)
Reference Link: https://www.geeksforgeeks.org/looping-techniques-python/

"""
print("\n" + "=" * 70)
print("TASK 19: Python - Looping Techniques")
print("=" * 70)

courses = ["Data Science", "Machine Learning", "Deep Learning", "Azure AI"]
codes = ["DS101", "ML201", "DL301", "AZ401"]

# 1. enumerate()
print("1. Using enumerate():")
for index, course in enumerate(courses, start=1):
    print(f"   {index}. Course Name: {course}")

# 2. zip()
print("\n2. Using zip() to pair courses with codes:")
for code, course in zip(codes, courses):
    print(f"   Code: {code} -> Course: {course}")

# 3. reversed()
print("\n3. Using reversed() without mutating original list:")
for item in reversed(courses):
    print(f"   Reverse item: {item}")

# 4. sorted()
scores = [88, 95, 72, 64, 91]
print("\n4. Using sorted() on scores:")
for score in sorted(scores):
    print(f"   Score: {score}", end=" | ")
print()

# 5. dict.items()
course_duration_weeks = {"Python": 4, "ML": 6, "DL": 4, "Azure": 2}
print("\n5. Using dict.items():")
for subject, weeks in course_duration_weeks.items():
    print(f"   Subject: {subject:<10} Duration: {weeks} weeks")


# =============================================================================
# TASK 20
# =============================================================================
"""
TASK 20: Python (Exercise on User Defined Functions)
Reference Link: https://www.geeksforgeeks.org/functions-in-python/

"""
print("\n" + "=" * 70)
print("TASK 20: Python - User Defined Functions")
print("=" * 70)

# 1. Simple function with calculation and return
def calculate_grade(score: float) -> str:
    """Determine grade based on numeric score."""
    if score >= 90:
        return "A+"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    else:
        return "C"

print("1. calculate_grade(85.5) ->", calculate_grade(85.5))

# 2. Function with default parameters
def greet_student(name: str, institution: str = "NAVTTC Center") -> str:
    """Greet student with default institution."""
    return f"Welcome, {name} to {institution}!"

print("2. greet_student('Ali') ->", greet_student("Ali"))
print("   greet_student('Sara', 'FAST NUCES') ->", greet_student("Sara", "FAST NUCES"))

# 3. Arbitrary Positional Arguments (*args)
def compute_average(*scores: float) -> float:
    """Calculate mean of any number of given numbers."""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)

print("3. compute_average(80, 90, 100, 70) ->", compute_average(80, 90, 100, 70))

# 4. Arbitrary Keyword Arguments (**kwargs)
def build_student_profile(roll_no: int, **details) -> dict:
    """Package student details dynamically into a profile dictionary."""
    profile = {"roll_no": roll_no}
    profile.update(details)
    return profile

student = build_student_profile(
    101,
    name="Muhammad Ayyan",
    course="Artificial Intelligence",
    city="Lahore",
    enrolled=True
)
print("4. build_student_profile(...) ->")
for k, v in student.items():
    print(f"   {k}: {v}")
print("=" * 70)

import numpy as np

# =============================================================================
# TASK 21
# =============================================================================
"""
TASK 21: Python (Exercise on List Data Type)
Reference Link: https://www.programiz.com/python-programming/list

"""
print("=" * 70)
print("TASK 21: Python - List Data Type Exercises")
print("=" * 70)

# 1. Creation and Indexing
numbers = [10, 20, 30, 40, 50]
print(f"Original list: {numbers}")
print(f"First element (index 0) : {numbers[0]}")
print(f"Last element (index -1) : {numbers[-1]}")

# 2. Slicing
print(f"Slice [1:4]             : {numbers[1:4]}")
print(f"Slice with step [::2]   : {numbers[::2]}")

# 3. List Methods
numbers.append(60)
print(f"After append(60)        : {numbers}")
numbers.extend([70, 80])
print(f"After extend([70, 80])  : {numbers}")
numbers.insert(2, 25)
print(f"After insert(2, 25)     : {numbers}")
removed_val = numbers.pop()
print(f"Popped last item ({removed_val}) : {numbers}")
numbers.remove(25)
print(f"After remove(25)        : {numbers}")

# 4. List Comprehension
squares = [x ** 2 for x in range(1, 6)]
print(f"List comprehension (squares of 1-5): {squares}")


# =============================================================================
# TASK 22
# =============================================================================
"""
TASK 22: Python (Exercise on Tuple Data Type)
Reference Link: https://www.programiz.com/python-programming/tuple

Week: 1
"""
print("\n" + "=" * 70)
print("TASK 22: Python - Tuple Data Type Exercises")
print("=" * 70)

# 1. Creation
single_item_tuple = ("AI",)  # note trailing comma
tech_tuple = ("Python", "Machine Learning", "Deep Learning", "Python")
print(f"Single-element tuple    : {single_item_tuple} (type: {type(single_item_tuple).__name__})")
print(f"Multi-element tuple     : {tech_tuple}")

# 2. Immutability
try:
    tech_tuple[0] = "Java"  # type: ignore
except TypeError as e:
    print(f"Immutability verified   : TypeError caught -> {e}")

# 3. Tuple Methods
print(f"Count of 'Python'       : {tech_tuple.count('Python')}")
print(f"Index of 'Deep Learning': {tech_tuple.index('Deep Learning')}")

# 4. Tuple Unpacking
point_3d = (12, 25, 50)
x, y, z = point_3d
print(f"Unpacked point_3d (x={x}, y={y}, z={z})")


# =============================================================================
# TASK 23
# =============================================================================
"""
TASK 23: Python (Exercise on String Data Type)
Reference Link: https://www.programiz.com/python-programming/string

"""
print("\n" + "=" * 70)
print("TASK 23: Python - String Data Type Exercises")
print("=" * 70)

message = "   National Vocational and Technical Training Commission   "

# 1. Slicing and Stripping
clean_msg = message.strip()
print(f"Raw string with spaces : '{message}'")
print(f"Stripped string        : '{clean_msg}'")
print(f"First 8 characters     : '{clean_msg[:8]}'")
print(f"Reversed string        : '{clean_msg[::-1][:15]}...'")

# 2. String Methods
print(f"Uppercase              : '{clean_msg.upper()}'")
print(f"Lowercase              : '{clean_msg.lower()}'")
print(f"Replaced string        : '{clean_msg.replace('Commission', 'Pakistan')}'")

words = clean_msg.split()
print(f"Split into words       : {words}")
joined = "-".join(words)
print(f"Joined with '-'        : '{joined}'")

# 3. String formatting
name = "Ayyan"
domain = "Artificial Intelligence"
print(f"F-String formatting    : Student {name} is enrolled in {domain}.")


# =============================================================================
# TASK 24
# =============================================================================
"""
TASK 24: Python (Exercise on Set Data Type)
Reference Link: https://www.programiz.com/python-programming/set

"""
print("\n" + "=" * 70)
print("TASK 24: Python - Set Data Type Exercises")
print("=" * 70)

# 1. Set Creation and Uniqueness
raw_data = [1, 2, 2, 3, 4, 4, 4, 5]
unique_set = set(raw_data)
print(f"List with duplicates   : {raw_data}")
print(f"Set (duplicates removed): {unique_set}")

# 2. Add and Discard
unique_set.add(6)
unique_set.discard(2)
print(f"After adding 6, removing 2: {unique_set}")

# 3. Set Operations
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

print(f"Union (A | B)                  : {set_a | set_b}")
print(f"Intersection (A & B)           : {set_a & set_b}")
print(f"Difference (A - B)             : {set_a - set_b}")
print(f"Symmetric Difference (A ^ B)   : {set_a ^ set_b}")


# =============================================================================
# TASK 25
# =============================================================================
"""
TASK 25: Python (Exercise on Dictionary Data Type)
Reference Link: https://www.programiz.com/python-programming/dictionary

"""
print("\n" + "=" * 70)
print("TASK 25: Python - Dictionary Data Type Exercises")
print("=" * 70)

# 1. Creation and Access
course_info = {
    "title": "AI, ML & Deep Learning",
    "duration_months": 3,
    "practical_ratio": "80%",
    "theory_ratio": "20%"
}
print(f"Course Dictionary: {course_info}")
print(f"Title using ['title']    : {course_info['title']}")
print(f"Safe access with .get()  : {course_info.get('certification', 'NAVTTC Certified')}")

# 2. Update and Remove
course_info["instructor"] = "Senior AI Trainer"
popped_ratio = course_info.pop("theory_ratio")
print(f"After update & pop: {course_info}")

# 3. Iterating
print("Iterating through dictionary:")
for key, value in course_info.items():
    print(f"   {key:<18} : {value}")

# 4. Dictionary Comprehension
square_dict = {x: x**2 for x in range(1, 6)}
print(f"Dictionary comprehension (n: n^2): {square_dict}")

