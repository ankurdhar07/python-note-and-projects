a = int(input("Enter the value of a: "))
match a:
    # x is the variable to match
    case 0:
        print("Case is zero")
    case 5:
        print("Case is 5")
    case _ if a <= 50:
        # case with if-condition
        print(a, "Number is nagative")
    case _ if a == 55:
        print(a, "Number is positive")    
    case _ if a != 60:    
        print(a, "is not equal to 60")
    case _:
        print(a)