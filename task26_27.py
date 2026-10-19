# =============================================================================
# TASK 26
# =============================================================================
"""
TASK 26: Python (Exercise on Exception Handling)
Reference Link: https://www.programiz.com/python-programming/exception-handling

"""
print("\n" + "=" * 70)
print("TASK 26: Python - Exception Handling Exercises")
print("=" * 70)

def divide_numbers(numerator: float, denominator: float):
    """Safely divide numbers with full try-except-else-finally handling."""
    print(f"\nAttempting division: {numerator} / {denominator}")
    try:
        result = numerator / denominator
    except ZeroDivisionError as err:
        print(f"   [Error Caught]: Cannot divide by zero! ({err})")
    except TypeError as err:
        print(f"   [Error Caught]: Invalid operand types! ({err})")
    else:
        print(f"   [Success]: Result is {result:.4f}")
    finally:
        print("   [Finally Block]: Cleanup / execution complete.")

divide_numbers(100, 4)
divide_numbers(100, 0)


# =============================================================================
# TASK 27
# =============================================================================
"""
TASK 27: Python (Exercise on User Defined Exception Handling)
Reference Link: https://www.programiz.com/python-programming/user-defined-exception

"""
print("\n" + "=" * 70)
print("TASK 27: Python - User Defined Exception Handling")
print("=" * 70)

# Custom Exception Class
class InvalidAgeError(Exception):
    """Exception raised when an applicant's age does not meet requirements."""
    def __init__(self, age: int, message: str = "Age must be between 18 and 35 to apply for NAVTTC program."):
        self.age = age
        self.message = message
        super().__init__(f"InvalidAgeError: {message} (Given Age: {age})")

def verify_candidate_eligibility(age: int):
    """Validate candidate age against NAVTTC admission criteria."""
    print(f"\nVerifying applicant with age = {age}...")
    try:
        if age < 18 or age > 35:
            raise InvalidAgeError(age)
        print(f"   Eligibility check passed for age {age}!")
    except InvalidAgeError as e:
        print(f"   [Handled Custom Exception]: {e}")

verify_candidate_eligibility(22)
verify_candidate_eligibility(15)
verify_candidate_eligibility(42)