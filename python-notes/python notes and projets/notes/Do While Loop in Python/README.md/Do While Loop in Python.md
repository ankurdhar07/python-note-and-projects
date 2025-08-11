# Python "Do While" Loop Simulation

## 📌 Introduction
Python does not have a built-in `do...while` loop like some other programming languages (e.g., C, Java).  
However, we can **simulate** its behavior using a `while True` loop combined with a `break` statement.

The key feature of a `do...while` loop is:
- The loop **executes at least once** before checking the condition.

---

## 🛠 Code Example
```python
while True:
    a = int(input("Enter a positive Number: "))
    print(a)
    if not (a > 0):
        break
📖 How It Works
1. Start Loop: The while True statement starts an infinite loop.

2. Take Input: The user is prompted to enter a number.

3. Display Output: The number entered is printed.

4. Condition Check:

- If the entered number is not positive, the break statement ends the loop.

- therwise, the loop continues.

5. Guarantee: The code inside the loop runs at least one time, no matter the input


🧠 Key Points

1. Simulates do...while loop behavior in Python.

2. Always runs at least once before checking the condition.

3. break is used to exit the loop when the condition fails.

4. Useful for input validation and menu-driven programs.


📂 Example Output:

Enter a positive Number: 5
5
Enter a positive Number: 7
7
Enter a positive Number: -2
-2

Author: Ankur Dhar
Note: Do While Loop in Python