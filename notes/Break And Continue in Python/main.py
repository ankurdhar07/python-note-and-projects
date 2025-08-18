for i in range(12):
    if (i == 5):
        print("Skip the iteration")
        continue
    print("12 *", i+1, "=", 12 * (i+1))
    if (i == 9):
        break

#example
# for i in range(1, 100, 1):
#     print(i , end = " ")
#     if (i == 50):
#         break
#     else:
#         print("CodeIsRunning")
# print("Thank You")        

# for i in [2, 4, 6, 8, 0]:
#     if (i%2!=0):
#         continue
#     print(i)

# i = 0 
# while True:
#     print(i)
#     i = i + 1
#     if (i%100 == 51):
#         break
# print("\n=== The loop has ended ===\n")


# Do while loop in use

while True:
    try:
        num = int(input("\nEnter a positive number :"))
    except ValueError:
        print("\nInvaid input! please try again!")
        continue
    if num > 0:
            print("\nYou entered a positive number\n")
            restart1 = input("\nDo you want to restart? (yes/no) :").lower().strip()
            if restart1 == "no":
                print("\nGoodBye... Thanks for playing :) \n")
                break
    elif num < 0:
         print("You entered a nagative number!!!")    
         restart2 = input("\nDo you want to restart? (yes/no) :").lower().strip()
         if restart2 == "no":
              print("\nGoodBye... Thanks for playing :) \n")
              break
         
# while True:
#     try:
#         num = int(input("\nEnter a nagative number :"))
#     except ValueError:
#         print("\nInvaid input! please try again!")
#         continue
#     if num < 0:
#             print("\nYou entered a nagative number\n")
#             restart1 = input("\nDo you want to restart? (yes/no) :").lower().strip()
#             if restart1 == "no":
#                 print("\nGoodBye... Thanks for playing :) \n")
#                 break
#     elif num > 0:
#                  print("\nYou entered a positive number!!!\n")
#                  restart2 = input("\nDo you want to restart? (yes/no) :").lower().strip()
#                  if restart2 == "no":
#                       print("\nGoodBye... Thanks for playing :) \n")
#                       break