# Strings Slicing and Operations on Strings in Python

This Python program demonstrates how to **slice strings**, find their length, and access specific characters using both **positive and negative indexing**.

## 📜 Description
The script covers:
- Slicing strings using `[start:end]` syntax.
- Determining the length of a string using `len()`.
- Accessing characters using **negative indexes**.
- Partial string extraction without specifying start or end indexes.

## 🧩 Code Example
```python
names = "Ankur, Rohan"
print(names[0:4])  # Slices characters from index 0 to 3

fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word")

print(fruit[-3:-1])  # Slices from the 3rd last to the 2nd last character

pie = "ApplePie"
print(pie[:5])       # From start to index 4
print(pie[3])        # Single character at index 3

nm = "Rahul"
print(nm[-4:-2])     # Negative index slicing (ans = "ah")

🚀 How to Run:

1. Make sure you have Python 3.x installed.

2. Save the file as main.py.

3. Open a terminal and run:
python main.py

📌 Key Concepts:

- String Slicing: string[start:end] returns characters from start to end-1.

- Negative Indexing: -1 represents the last character, -2 the second last, and so on.

- Length Function: len(string) returns the total number of characters in the string.

- Leaving start or end blank will slice from the beginning or till the end respectively.

Author: Ankur Dhar
Python Version: 3.x