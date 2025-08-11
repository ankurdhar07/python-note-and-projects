# Type Casting in Python

This Python program demonstrates **type casting** (type conversion) in Python — converting values from one data type to another.

## 📜 Description
The script covers:
- Converting strings to integers using `int()`.
- Automatic (implicit) type conversion by Python.
- Checking data types using `type()`.

## 🧩 Code Example
```python
a = 3
b = 3
print(int(a) + int(b))

string = "15"
number = 7
string_number = int(string)  # Explicit type casting
sum = number + 15
print("The sum of both numbers is", sum)

# Python automatically converts a to int
a = 7
print(type(a))

# Python automatically converts b to float
b = 3.0
print(type(b))

# Python automatically converts c to float as it is a float addition
c = a + b
print(c)
print(type(c))

🚀 How to Run

1. Ensure Python 3.x is installed.

2. Save this script as type_casting.py.

3. Run the script:
python type_casting.py

💡 Example Output

6
The sum of both numbers is 22
<class 'int'>
<class 'float'>
10.0
<class 'float'>


| Term                      | Description                                                                               |
| ------------------------- | ----------------------------------------------------------------------------------------- |
| **Explicit Type Casting** | Manually converting a value to a specific type using functions like `int()` or `float()`. |
| **Implicit Type Casting** | Python automatically changes the data type when needed during operations.                 |
| `type()`                  | Returns the data type of a variable.                                                      |
| **int()**                 | Converts a value to an integer.                                                           |
| **float()**               | Converts a value to a floating-point number.                                              |


Author: Ankur Dhar
Python Version: 3.x