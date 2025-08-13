# 📘 Functions in Python

This note demonstrates how to define and use **functions** in Python, along with examples of conditional statements (`if-else`) and parameter passing.

---

## 🔹 Table of Contents
1. [Introduction](#introduction)
2. [Calculating Gmean](#calculating-gmean)
3. [Conditional Checks](#conditional-checks)
4. [Functions for Comparison](#functions-for-comparison)
5. [Example Output](#example-output)

---

## Introduction
Functions in Python help in reusing code, improving readability, and organizing logic into reusable blocks.

**Syntax:**
```python
def function_name(parameters):
    # code block
    return value
Calculating Gmean

Example:
def calculateGmean(a, b):
    mean = (a * b) / (a + b)
    print(mean)

# Calling the function
calculateGmean(2, 4)
calculateGmean(8, 6)

Conditional Checks

We can combine if-else with functions to compare two numbers:
a = 4
b = 3
if a > b:
    print("First number is greater than second number")
else:
    print("First number is not greater than second number or equal")

calculateGmean(a, b)

Functions for Comparison

Two comparison functions are defined:
def isGreater(a, b):
    if a > b:
        print("First number is greater than second number")
    else:
        print("First number is not greater than second number or equal")

def isLesser(a, b):
    pass  # Placeholder function

def name(Sam, Ram):
    print("Hello", Sam, Ram)

Example Call:
isGreater(6, 3)
name("Rahul", "Sonu")

Example Output:
1.3333333333333333
2.6666666666666665
First number is greater than second number
1.7142857142857142
First number is not greater than second number
2.727272727272727
First number is greater than second number
Hello Rahul Sonu
📌 Key Points

- Functions are reusable and prevent code repetition.

- Use if-else for conditional logic.

- You can define placeholders using pass.

- Functions can accept multiple parameters.

Author: Ankur Dhar
Note: For Loops in Python