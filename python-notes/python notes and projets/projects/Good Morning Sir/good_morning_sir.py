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