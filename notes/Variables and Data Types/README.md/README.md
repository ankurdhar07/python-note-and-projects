# Variables and Data Types in Python

This Python program demonstrates how variables work, how to check their data types, and the use of different built-in Python data types.

## 📌 Topics Covered
- What is a variable?
- Data types in Python
- Using the `type()` function
- Conditional statements (`if-else`)
- Collections in Python:
  - **List**
  - **Dictionary**
  - **Tuple**
- Escape characters in strings

---

## 📄 Code Explanation

### 1️⃣ Declaring Variables
Variables are like containers that store data in memory.
```python
a = 1
b = "Ankur"
c = None
d = True

Here:

- a is an integer (int)

- b is a string (str)

- c is None (NoneType)

- d is a boolean (bool)

2️⃣ Checking Data Types
We can check the type of a variable using the type() function:
print(type(c))
print(type(b))
print(type(a))

3️⃣ Numeric Data Types
- int → Whole numbers (e.g., 3, -8, 0)

- float → Decimal numbers (e.g., 7.349, -9.0)

- complex → Numbers with imaginary part (e.g., 6 + 2j)

4️⃣ Boolean Data
Boolean values are either:
True
False

5️⃣ Conditional Statements
if (3 > 7):
    print("f is greater than g")
else:
    print("f is not greater than g")

This checks if a condition is True or False and executes code accordingly.

6️⃣ Collections in Python

📋 List (Mutable, ordered)

list1 = ["apple", "Ankur", {"name"}, {"Ankur"}]

📚 Dictionary (Key-Value pairs, unordered)
dict1 = {"Name": "Krishu", "Age": 15, "canvote": True}

🗂 Tuple (Immutable, ordered)
tuple = (("Ankur", "Krishu"), ("Horse", "Lion", "Cat"))

7️⃣ Printing Strings
print("Hello World")
print("Early to bed\nearly to rise\nwake up morning")

Here, \n is used to move to the next line.

🖥 Example Output
<class 'NoneType'>
<class 'str'>
<class 'int'>
f is not greater than g
['apple', 'Ankur', {'name'}, {'Ankur'}]
{'Name': 'Krishu', 'Age': 15, 'canvote': True}
(('Ankur', 'Krishu'), ('Horse', 'Lion', 'Cat'))
Hello World
Early to bed
early to rise
wake up morning

📚 Summary

- This program helps in understanding:

- How to create and use variables

- Checking data types

- Working with basic Python collections

- Using conditional statements

- Printing with escape characters

Author: Ankur Dhar
Note: Break And Continue in Python