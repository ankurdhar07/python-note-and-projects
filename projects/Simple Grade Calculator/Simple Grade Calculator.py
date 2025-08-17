marks = int(input("Enter your marks between 0 to 100 :"))
if 90 <= marks <= 100:
    print("Grade A")
elif 80 <= marks <= 89:
    print("Grade B")
elif 70 <= marks <= 79:
    print("Grade C")
elif 60 <= marks <= 69:
    print("Grade D")
elif 50 <= marks <= 59:
    print("Grade E")        
elif marks < 50:
    print("Fail!")
else:
    print("You entered a invalid number!")