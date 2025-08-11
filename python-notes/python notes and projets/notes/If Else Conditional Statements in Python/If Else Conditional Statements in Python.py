num = int(input("Enter your value of number :" ))
if(num < 0):
    print("Number is nagative")
elif(num == 700):
    print("Number is special")
else:
    print("Number is positive")    
# conditional operators:
# <, >, <=, ==,!=
a = int(input("Enter you age"))
print("Your age is", a)
print(a < 18)
print(a > 18)
print(a <= 18)
print(a != 18)
if(a <= 18):
    print("You cannot drive")
else:
    print("you can drive")