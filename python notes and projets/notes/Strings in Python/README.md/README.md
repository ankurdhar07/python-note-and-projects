# Strings in Python

This Python program demonstrates **string creation, indexing, and iteration** in Python.

## 📜 Description
The script covers:
- Creating strings using **single quotes**, **double quotes**, and **triple quotes**.
- Printing multiline strings.
- Accessing characters using **indexing**.
- Looping through a string using a **for loop**.

## 🧩 Code Example
```python
name = ("Ankur")
friend = ("Satyam")
anothername = ("Rohan")

Apple = '''he said
Hii Ankur...
What you want to do today?
I want to eat an apple'''

print(Apple)
print("Heyy watsapp?", friend)

# Accessing individual characters from a string
print(friend[0])
print(friend[1])
print(friend[2])
print(friend[3])
print(friend[4])
print(friend[5])
# print(friend[6])  # This will throw an IndexError

# Using a for loop to iterate over a string
print("Lets use for loop\n")
for character in Apple:
    print(character)

    print(character)

🚀 How to Run
1. Make sure you have Python 3.x installed.

2. Save the file as strings_example.py.

3. Open a terminal and run:
python strings_example.py

📌 Key Concepts
- Triple quotes (''' or """) allow writing multiline strings.

- Strings are zero-indexed in Python (friend[0] is the first character).

- Accessing an index that does not exist will cause an IndexError.

- Strings are iterable, so you can loop through each character.

Author: Ankur Dhar
Python Version: 3.x