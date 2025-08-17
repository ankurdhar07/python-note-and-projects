# If Else Conditional Statements in Python

This note explains how to use **if**, **elif**, and **else** statements in Python, along with conditional operators.

## 📌 Features Covered

1. **Basic Conditional Statements**
   - `if` → Executes a block of code if the condition is `True`.
   - `elif` → Checks another condition if the previous `if` was `False`.
   - `else` → Executes if all previous conditions are `False`.

2. **Conditional Operators**
   - `<` → Less than
   - `>` → Greater than
   - `<=` → Less than or equal to
   - `==` → Equal to
   - `!=` → Not equal to

---

## 📝 Example Code

```python
# Number check
num = int(input("Enter your value of number: "))
if num < 0:
    print("Number is negative")
elif num == 700:
    print("Number is special")
else:
    print("Number is positive")

# Conditional operators example
a = int(input("Enter your age: "))
print("Your age is", a)
print(a < 18)
print(a > 18)
print(a <= 18)
print(a != 18)

# Driving eligibility check
if a <= 18:
    print("You cannot drive")
else:
    print("You can drive")

💻 Example Output:

your value of number: -5
Number is negative
Enter your age: 17
Your age is 17
True
False
True
True
You cannot drive

📖 Notes:

- Use if-elif-else to handle multiple conditions in a clean and structured way.

- Conditional operators help compare values and make decisions in code.

- Always ensure the input is converted to the correct data type before comparison.

Author: Ankur Dhar
Note: If Else Conditional Statements in Python