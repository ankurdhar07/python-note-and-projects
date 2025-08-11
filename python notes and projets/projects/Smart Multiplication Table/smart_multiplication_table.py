while True:
    try:
        num = int(input("\nEnter a number for its Multiplication Table :"))
    except ValueError:
        print("Invaild input! please enter a vaild number only")
        continue
    print(f"\nMultiplication table of {num}")
    for i in range(1, 11):
        print(f"{num} * {i} = {num * i}")
    print("\nCountdown before exiting this round :")
    count = 5
    while count > 0:
        print(count)
        count -= 1
    again = input("\nDo you want to genarate another table? (yes/no) :")
    if again != "yes":
        print("GoodBye...")
        break   
