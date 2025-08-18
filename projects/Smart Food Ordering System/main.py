print("=== Welcome to Ankur's cafe ===")
print("\nMenu ---\n\ncold coffee : 10$\nburger : 20$\npizza : 32$\nicecream : 5$")
order = input("\nSoo... what do you want to order? : ").lower()
if order == "cold Coffee":
    print("You ordered a cold coffee - price 10$")
elif order == "burger":
    print("You ordered a burger - price 20$")
elif order == "pizza":
    print("You ordered a pizza - price : 32$")
elif order == "icecream":
    print("You orderd a icecream - price : 5$")   
else:
    print("Sorry, this item is not available :(")     