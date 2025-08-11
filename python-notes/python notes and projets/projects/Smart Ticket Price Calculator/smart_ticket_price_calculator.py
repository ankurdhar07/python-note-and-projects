age = int(input("Enter your age :"))
time = input("Enter time of the day (morning / afternoon / evening) :").lower()
if age <= 12:
    if time == "morning":
        price = 100
    else:
        price = 150
elif age <= 18:
    if time == "morning":
        price = 150
    else:
        price = 200               
elif age <= 19:
    if time == "morning":
        price = 200
    elif time == "evening":
        price = 250
    else:
        price = 200            
elif age <= 60:
    if time == "morning":
        price = 200
    elif time == "evening":
        price = 250
    else:
        price = 200
else:
    price = 120
print("your ticket price is", price)