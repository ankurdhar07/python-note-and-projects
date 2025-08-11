# strings are immutable
a = "Ankur!!!!!!! Ankur Ankur!!!"
b = "facebook"
c = "Welcome to the console!!!"
print(len(a))
print(a.upper()) #The upper() method converts a string to upper case
print(a.lower()) #The lower() method converts a string to lower case
print(a.rstrip("!")) #the rstrip() removes any trailing characters. Example:
print(a.replace("Ankur", "john")) #The replace() method replaces all occurences of a string with another string. Example:
print(a.split(" ")) #The split() method splits the given string at the specified instance and returns the separated strings as list items
print(b.capitalize()) #The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase
print(b.center(50)) #The center() method aligns the string to the center as per the parameters given by the user
print(a.count("Ankur")) #The count() method returns the number of times the given value has occurred within the given string
print(a.endswith("!")) #The endswith() method checks if the string ends with a given value. If yes then return True, else return False
print(c.endswith("the", 1, 4)) #We can even also check for a value in-between the string by providing start and end index positions
print(c.find("to")) #The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.
print(c.find("tohhh")) #As we can see, this method is somewhat similar to the index() method. The major difference being that index() raises an exception if value is absent whereas find() does not
# print(c.index("tohhh"))
str1 = "WelcomeToTheConsole, 7"
print(str1.isalnum()) #The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False
print(str1.isalpha()) #The isalnum() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False
print(b.islower()) #The islower() method returns True if all the characters in the string are lower case, else it returns False
print(b.isupper()) #The isupper() method returns True if all the characters in the string are upper case, else it returns False
print(b.isprintable()) #The isprintable() method returns True if all the values within the given string are printable, if not, then return False
str2 = "      " #using spacebar
str3 = "        " #using tab
print(str2.isspace()) #The isspace() method returns True only and only if the string contains white spaces, else returns False
print(c.index("the")) #The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception
str4 = "To Kill A Mocking Bird"
print(str4.istitle()) #The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False
print(c.startswith("Welcome")) #The endswith() method checks if the string starts with a given value. If yes then return True, else return False
print(a.swapcase()) #The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case
t = "His name is dan. Dan is a honest man"
print(t.title()) #The title() method capitalizes each letter of the word within the string
f = ("Krishu")
print(f)