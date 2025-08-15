l = [2, 4, 6]
print(type(l))
print(l)
print(l[:])
print(l[0])
print(l[1])
print(l[2])

colour = ["Red", "Green", "Yellow", "Blue"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(colour)
print(colour[2])
print(numbers)
print(numbers[5])
print(numbers[len(numbers)-3])
print(numbers[10-3])
print(numbers[2:4])
print(numbers[1:-4])
print(numbers[1:8])
print(numbers[1:8:2])
print(numbers[-3])
print(numbers[7])

if 11 in numbers:
    print("Yes")
else:
    print("No")

if "Green" in colour:
    print("Yes")
else:
    print("No")

# Same thing applies for string as well!
if "reen" in "Green":
    print("Yes")
else:
    print("No")

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])	#using positive indexes
print(animals[-6:-2])	#using negative indexes'

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[4:])	#using positive indexes
print(animals[-4:])	#using negative indexes

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[:6])	#using positive indexes
print(animals[:-3])	#using negative indexes

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[::2])		#using positive indexes
print(animals[-8:-1:2])	#using negative indexes

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[1:8:3])
# ans = (dog, pig, goat)

lst = [i for i in range(8)]
print(lst)

lst = [i+1 for i in range(8)]
print(lst)

lst = [i*2 for i in range(8)]
print(lst)

lst = [i*2 for i in range(8) if i % 2 == 0]
print(lst)

lst = [i-1 for i in range(8)]
print(lst)

lst = [i/2 for i in range(8)]
print(lst)

names = ["Ankur", "Milo", "Sharah", "Bruno", "Rosa", "John", "Dan"]
namesWith_0 = [item for item in names if "o" in item]
print(namesWith_0)

names = ["Ankur", "Milo", "Sharah", "Bruno", "Rosa", "John", "Dan"]
namesWith_0 = [item for item in names if len(item) > 4]
print(namesWith_0)