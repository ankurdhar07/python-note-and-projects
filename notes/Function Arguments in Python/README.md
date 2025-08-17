# Function Arguments in Python

This note demonstrates various ways to define and use function arguments in Python, including **default arguments**, **positional arguments**, **keyword arguments**, **arbitrary positional arguments (`*args`)**, and **arbitrary keyword arguments (`**kwargs`)**.

---

## 1. Basic Function Arguments:

A simple example of passing two parameters to a function:
```python
def average(a, b):
    print("The average is", (a + b) / 2)

average(2, 4)  # Output: The average is 3.0


2. Default Arguments:

Default arguments allow parameters to have a default value if not provided by the caller.

def average(a, b, c=5):
    print("The average is", (a + b + c) / 2)

average(3, 5)  # Output: The average is 6.5


3. Keyword Arguments:

Keyword arguments allow passing values to specific parameters by name, regardless of their order.

def name(fname, mname="Subham", lname="Rahul"):
    print("Hello,", fname, mname, lname)

name("Ankur", "Dan", "Satyam")  # Output: Hello, Ankur Dan Satyam


4. Positional Arguments:

The order of the arguments matters here.

def name(fname, mname, lname):
    print("Hello", fname, mname, lname)

name("Krishu", "Ankur", "Sonu")  # Output: Hello Krishu Ankur Sonu


5. Arbitrary Positional Arguments (*args):

Use *args to accept multiple positional arguments in a tuple.

def average(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum / len(numbers)

c = average(2, 4)
print(c)  # Output: 3.0


6. Arbitrary Keyword Arguments (**kwargs):

Use **kwargs to accept multiple keyword arguments in a dictionary.

def name(**name):
    print(type(name))  # Output: <class 'dict'>
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname="John", lname="Rick", fname="Ayon")
# Output:
# <class 'dict'>
# Hello, Ayon John Rick


📌 Key Takeaways:

- Default arguments provide flexibility when parameters may have a common value.

- Positional arguments rely on order, while keyword arguments rely on explicit names.

- *args collects multiple positional arguments into a tuple.

- **kwargs collects multiple keyword arguments into a dictionary.


Author: Ankur Dhar
Note: Function Arguments in Python