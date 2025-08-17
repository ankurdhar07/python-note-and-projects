Good Morning Sir
A simple Python program that greets the user based on the current time of the day.

📌 Features:
Automatically detects the current system time.

Greets appropriately:

Good Morning Sir (5:00 AM – 11:59 AM)

Good Evening Sir (12:00 PM – 3:59 PM)

Good Afternoon Sir (4:00 PM – 5:59 PM)

Good Night Sir (6:00 PM – 4:59 AM)

🖥️ How It Works:

The program uses Python’s built-in datetime module to get the current hour.

Based on the hour, it selects a greeting message.

Prints the greeting directly to the console.

💻 Code Example:

from datetime import datetime

current_time = datetime.now().hour

if 5 <= current_time < 12:
    print("Good morning sir")
elif 12 <= current_time < 16:
    print("Good evening sir")
elif 16 <= current_time < 18:
    print("Good afternoon sir")
else:
    print("Good night sir")

🚀 How to Run:

1. Make sure you have Python 3 installed.

2. Save the code in a file, for example:
main.py
3. Open a terminal or command prompt in the file’s directory.
4. Run:
python main.py

📂 File Structure:

Good-Morning-Sir/
│-- main.py
│-- README.md


📜 License
This project is licensed under the MIT License — you are free to use and modify it.


👤 Author
Ankur Dhar
📧 Email: ankurdhar69@gmail.com
💻 GitHub: ankurdhar07