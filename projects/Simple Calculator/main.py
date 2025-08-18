print(" ===Simple Calculator=== ")
try:
    a = int(input("Enter your first number :"))
except ValueError:
    print("Please enter your number correctly!")
try:
    b = int(input("Enter your second number :"))
except ValueError:
    print("Please enter your numeber correctly")
print("\n1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
try:
    operation = int(input("\nEnter your operation :"))
except ValueError:
    print("Please enter your number corerctly!")
if operation == 1:
    print(f"\nResult :{a+b}")
elif operation == 2:
    print(f"\nResult :{a-b}")
elif operation == 3:
    print(f"\nResult :{a*b}")
elif operation == 4:
    print(f"\nResult :{a/b}")
else:
    print("\nYou choosed a wrong operation\n")

print("\nThanks for playing :)\n")