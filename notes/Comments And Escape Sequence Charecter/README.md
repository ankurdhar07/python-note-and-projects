# Comments And Escape Sequence Character in Python

This note demonstrates:
- How to use **escape sequences** in strings.
- How to handle special characters (like quotes) inside a string.
- How to use the `sep` and `end` parameters in the `print()` function.

## 📌 Features Covered

1. **Escape Sequences**
   - `\"` → Insert double quotes inside a string surrounded by double quotes.
   - `\'` → Insert single quotes inside a string surrounded by single quotes.

2. **`sep` Parameter**
   - Defines a custom separator between multiple values in `print()`.

3. **`end` Parameter**
   - Specifies what is printed after the final value, instead of the default newline.

---

## 📝 Example Code

```python
# Escape sequence examples
print("Heyy! \"I am Ankur\"")
print("Heyy! \'I am Ankur\'")

# Using 'sep' parameter
a = 4
b = 4
print(a, b, sep="-")  # Output: 4-4

# Using 'end' parameter
print(a + b, end="\n43")  # Output: 8

💻 Example Output:

Heyy! "I am Ankur"
Heyy! 'I am Ankur'
4-4
8
43

📖 Notes:

- Escape sequences are useful when working with special characters inside strings.

- The sep parameter is handy for formatting output.

- The end parameter allows you to control what follows after the print statement.

Author: Ankur Dhar
Note: Comments And Escape Sequence Charecter