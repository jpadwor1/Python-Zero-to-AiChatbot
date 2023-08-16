"""
Homework 5:
Building More Interactivity for Our AI Chatbot:


1. Your First Function:

Write a function named square_number that takes a number as a parameter and returns its square. Test your function with a few numbers to ensure it works correctly.
"""


def square_number(number):
    return number ** 2

userNumber = int(input("Enter a number. "))

print(square_number(userNumber))

"""
2. Personalized Chatbot Function:

Create a function named chatbot_response that takes a user's mood as a parameter (e.g., happy, sad, excited) and returns a personalized message based on that mood.
"""
def chatbot_response(mood):
    if mood == "happy":
        print("That is wonderful!")
    elif mood == "sad":
        print("I am sorry to hear that.")
    else:
        print("That's good news!")

userMood = input("How are you feeling today? Happy, sad, excited, etc.?")

chatbot_response(userMood)

"""
3. Advanced Function Practice:

Write a function named calculate_area that takes the length and width of a rectangle as parameters and returns its area. Test your function with different lengths and widths.
"""

def calculate_area(length,width):
    return length * width

width = int(input("Enter the rectangle width."))
length = int(input("Enter the rectangle length."))

print(calculate_area(length, width))
