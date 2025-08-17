# Break And Continue in Python

This project demonstrates the use of **`break`** and **`continue`** statements in Python, along with examples of `for`, `while`, and simulated `do-while` loops.

---

## 📌 Overview

In Python:
- **`break`** is used to exit a loop prematurely when a certain condition is met.
- **`continue`** is used to skip the current iteration and move to the next one.
- Python does not have a native **do-while** loop, but it can be simulated using a `while True` loop with a `break` condition.

This note contains multiple examples:
1. `for` loop with `continue` and `break`.
2. Iterating through a list with `continue`.
3. Infinite `while` loop with `break`.
4. Simulated `do-while` loop for user input validation.

---

## 📂 Code Structure

### 1️⃣ For Loop with `continue` and `break`:
```python
for i in range(12):
    if (i == 5):
        print("Skip the iteration")
        continue
    print("12 *", i+1, "=", 12 * (i+1))
    if (i == 9):
        break

Explanation:

- Skips printing when i is 5.

- Stops the loop when i reaches 9.

2️⃣ For Loop with a List and continue:

for i in [2, 4, 6, 8, 0]:
    if (i % 2 != 0):
        continue
    print(i)

Explanation:
Prints only even numbers, skipping odd ones.

3️⃣ Infinite While Loop with Break:

i = 0
while True:
    print(i)
    i = i + 1
    if (i % 100 == 51):
        break
print("\n=== The loop has ended ===\n")

Explanation:
Counts up and stops when the remainder of i divided by 100 equals 51.

4️⃣ Simulated Do-While Loop:

while True:
    try:
        num = int(input("\nEnter a positive number :"))
    except ValueError:
        print("\nInvalid input! please try again!")
        continue
    if num > 0:
        print("\nYou entered a positive number\n")
        restart1 = input("\nDo you want to restart? (yes/no) :").lower().strip()
        if restart1 == "no":
            print("\nGoodBye... Thanks for playing :) \n")
            break
    elif num < 0:
        print("You entered a negative number!!!")    
        restart2 = input("\nDo you want to restart? (yes/no) :").lower().strip()
        if restart2 == "no":
            print("\nGoodBye... Thanks for playing :) \n")
            break

Explanation:

- Keeps asking for input until the user enters "no".

- Handles both positive and negative number cases.

- Uses strip() to remove extra spaces and .lower() to handle case-insensitive responses.

▶️ How to Run:

1. Save the script as main.py.

2. Open your terminal and run:
python main.py

3. Follow the on-screen instructions.

📝 Notes:

- break exits the loop completely.

- continue skips only the current iteration.

- A do-while loop in Python can be achieved using while True with an exit condition.

📷 Example Output:

12 * 1 = 12
12 * 2 = 24
12 * 3 = 36
12 * 4 = 48
Skip the iteration
12 * 6 = 72
12 * 7 = 84
12 * 8 = 96
12 * 9 = 108
12 * 10 = 120

Enter a positive number : 5
You entered a positive number

Do you want to restart? (yes/no) : no
GoodBye... Thanks for playing :)

Author: Ankur Dhar
Note: Break And Continue in Python