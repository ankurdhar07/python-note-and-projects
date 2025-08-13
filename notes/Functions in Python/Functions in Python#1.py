a = 2
b = 4
c = 8
d = 6
gmean = (a * b)/(a + b)
print(gmean)
gmean = (c * d)/(c + d)
print(gmean)

a = 2
b = 4
c = 8
d = 6
def calculateGmean (a , b):
    mean = (a * b)/(a + b)
    print(mean)
calculateGmean(a, b)
calculateGmean(c, d)    

def calculateGmean(a, b):
    mean = (a * b)/(a + b)
    print(mean)
a = 4
b = 3
if (a > b ):
    print("\nFirst number is greater than second number\n")
else:
    print("\nFirst number is not greater than second number or equal\n")    
calculateGmean(a, b)

c = 5
d = 6
if (c > d):
    print("First number is greater than second number")
else:
    print("First number is not greater than second number")
calculateGmean(c, d)

def isGreater(a, b):
    if (a > b ):
        print("\nFirst number is greater than second number\n")
    else:
        print("\nFirst numeber is not greater than second number or equal\n")    
a = 6
b = 3
isGreater(a, b)

def isLesser(a, b):
    pass
def name(Sam, Ram):
    print("Hello", Sam, Ram)

name("Rahul", "Sonu")