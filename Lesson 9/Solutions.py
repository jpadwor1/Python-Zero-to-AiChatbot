"""
Homework for Video 9:

Alarm Clock:
Task: Create a simple alarm clock that takes in a time and waits until that time to sound an alarm (print a message).
Tips
1. Import necessary libraries.
"""
import time
import datetime
"""
2. Get the current system time.
"""
current_time = datetime.datetime.now()

"""
3. Prompt the user to input the desired alarm time (consider using a specific format, e.g., HH:MM).
"""
selected_time = input("When do you need the alarm? Enter HH:MM : ")
"""
4. Convert the user's input into a comparable time format.
"""
formatted_time = datetime.datetime.strptime(selected_time, "%H:%M").time()
"""
5. Use a loop to constantly check the system time.
"""
while True:
    current_time = datetime.datetime.now().time()
    if current_time.hour == formatted_time.hour and current_time.minute == formatted_time.minute:
        break
    time.sleep(30)


"""

6. If the system time matches the alarm time, print the alarm message and exit the loop.
"""
print("ALARM! Time to wake up")

"""
Birthday Countdown:
Task: Ask the user for their birthdate and calculate how many days are left until their next birthday.

Tips
1. Prompt the user for their birthdate (consider specifying a format, e.g., YYYY-MM-DD).
"""
user_birthdate = input("Please enter your birthdate as YYYY-MM-DD :")
"""
2. Convert the user's input into a date format.
"""
formatted_birthdate = datetime.datetime.strptime(user_birthdate, "%Y-%m-%d")

"""
3. Get the current system date.
"""
current_date = datetime.datetime.today() 

"""
4. Determine the user's next birthday (might be this year or the next year).
"""
if formatted_birthdate.month > current_date.month or (formatted_birthdate.month == current_date.month and formatted_birthdate.day > current_date.day):
    next_birthday = datetime.date(current_date.year, formatted_birthdate.month, formatted_birthdate.day)
else:
    next_birthday = datetime.date(current_date.year + 1, formatted_birthdate.month, formatted_birthdate.day)

"""
5. Calculate the difference in days between the current date and the next birthday.
"""
days_until_birthday = (next_birthday - current_date).days
"""
6. Print the number of days left until the user's next birthday.
"""
print(f"There are {days_until_birthday} days left until your next birthday!")
"""
Area Calculator:
Task: Design a program that calculates the area of different shapes (circle, square, rectangle). Use the math module for necessary calculations.
Tips
1. Import the math module.
2. Print a menu for the user with choices (e.g., 1 for circle, 2 for square, etc.).
3. Ask the user to select a shape.
4. Based on the user's choice:
    a. If it's a circle:
        Prompt for the radius.
        
    b. If it's a square:
        Prompt for the side length.

    c. If it's a rectangle:
        Prompt for the width and height.
5. Calculate the area using width * height.
6. Print the calculated area for the selected shape.
"""