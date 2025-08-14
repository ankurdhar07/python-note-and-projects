def average(a, b):
    print("The average is", (a + b)/2)
average(2, 4)


def average(a, b, c = 5):
    print("The average is", (a + b + c)/2)
# average(2, 4)
# average(b = 2)
# average(b = 2, a = 6)
average(3,5)

def name(fname, mname = "Subham", lname = "Rahul"):
    print("Hello,", fname, mname, lname)
name("Ankur", "Dan", "Satyam")

def name(fname, mname, lname):
    print("Hello", fname, mname, lname)
name("Krishu", "Ankur", "Sonu")

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    # print("Average is :", sum / len(numbers))
    return sum / len(numbers)
c = average(2, 4)
print(c)

def name(**name):
    print(type(name))
    print("Hello,", name["fname"], name["mname"], name["lname"])
name(mname = "John", lname = "Rick", fname = "Ayon")