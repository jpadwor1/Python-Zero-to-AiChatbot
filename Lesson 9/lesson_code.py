import time

print("Starting...")
time.sleep(2)  # Pauses the program for 2 seconds
print("...Finished!")


current_time = time.time()
# This will give us the number of seconds since January 1, 1970 (the epoch)
print(f"Current time in seconds since the epoch: {current_time}")


import datetime

today = datetime.date.today()
# This gives us the current date in the format YYYY-MM-DD
print(f"Today's date is: {today}")

# Formatting the date to a more readable form
formatted_date = today.strftime("%B %d, %Y")
print(f"Formatted date: {formatted_date}")  
# Expected Output: Formatted date: Month DD, YYYY

"strptime stands for 'string parse time'. It allows us to convert a date string into a date object. The trick is to tell Python the format of our date string."


date_string = "24-12-2022"
date_object = datetime.datetime.strptime(date_string, "%d-%m-%Y")
print(f"Converted date: {date_object.date()}")  # Expected Output: Converted date: 2022-12-24

import math

# ceil rounds up, while floor rounds down
print(math.ceil(4.2))   # Outputs: 5
print(math.floor(4.8))  # Outputs: 4


# Pi is a mathematical constant; it's the ratio of a circle's circumference to its diameter
print(math.pi)  # Outputs the value of pi
