# Taking User Input in Python

This Python program demonstrates how to **take user input** and perform arithmetic operations using both **integers** and **floating-point numbers**.

## 📜 Description
The script:
- Accepts **two numbers** as input from the user.
- Converts them to `int` and `float` types for calculations.
- Performs **addition, multiplication, and modulo** operations.

## 🧩 Code Example
```python
a = input("Enter your first number: ")
b = input("Enter your second number: ")

# Integer operations
print(int(a) + int(b))   # Addition
print(int(a) * int(b))   # Multiplication
print(int(a) % int(b))   # Modulo

# Float operations
print(float(a) + float(b))  # Addition
print(float(a) * float(b))  # Multiplication
print(float(a) % float(b))  # Modulo

🚀 How to Run:

1. Make sure you have Python 3.x installed.

2. Save the file as main.py.

3. Open a terminal and run:
python main.py


💡 Example Output:

Enter your first number: 5
Enter your second number: 3
8
15
2
8.0
15.0
2.0

📌 Key Concepts:

- input() always returns a string, so type conversion (int() / float()) is needed for numeric operations.

- int() converts the string to an integer.

- float() converts the string to a floating-point number.

- % (Modulo) returns the remainder of a division.

Author: Ankur Dhar
Python Version: 3.x

