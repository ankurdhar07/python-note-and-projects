# Match Case Statements in Python

This note explains how to use **`match`** and **`case`** statements in Python (introduced in Python 3.10) for pattern matching.

## 📌 Features Covered

1. **Basic Match-Case**
   - Compares a value against different `case` patterns.
   - Executes the first case that matches.

2. **Wildcard `_`**
   - Matches anything if no other case matches.

3. **Case with Condition (`if`)**
   - Allows adding conditional logic inside a `case`.

---

## 📝 Example Code

```python
a = int(input("Enter the value of a: "))

match a:
    # Case when a is exactly 0
    case 0:
        print("Case is zero")

    # Case when a is exactly 5
    case 5:
        print("Case is 5")

    # Case with condition (if a <= 50)
    case _ if a <= 50:
        print(a, "Number is negative")

    # Case when a is exactly 55
    case _ if a == 55:
        print(a, "Number is positive")

    # Case when a is not equal to 60
    case _ if a != 60:
        print(a, "is not equal to 60")

    # Default case (when nothing matches above)
    case _:
        print(a)

💻 Example Output

Enter the value of a: 5
Case is 5

Enter the value of a: 40
40 Number is negative

Enter the value of a: 100
100 is not equal to 60

📖 Notes
- match-case is similar to switch-case in other languages.

- The first matching case is executed, and the rest are skipped.

- _acts as a wildcard (matches anything).

- Can combine case with conditions using if.

🛠 Python Version Requirement
Important: match-case works only in Python 3.10+.

Author: Ankur Dhar
Note: Match Case Statements in Python