"""
Homework 2:
Building More Interactivity for Our AI Chatbot:


1. Traffic Light Decisions:

Write a program that asks the user for the current traffic light color (red, yellow, green) and then tells the user what action they should take (stop, slow down, go).
""" 
currentLight == input("What is the current traffic light color? (red, yellow, green) ")

if currentLight == "red":
    print("Stop")
elif currentLight == "yellow":
    print("Slow down")
else:
    print("Go")

"""
2. Chatbot Mood Enhancements:

Expand the chatbot mood interaction from Lesson 1 exercise 2. If the user says they're "tired", the chatbot should respond with "Maybe you should take a break." If the user says they're "excited", the chatbot should say "That's awesome! What's the occasion?"
"""
userMood == input("How are you feeling today? ")

if userMood == "tired":
    print("Maybe you should take a break.")
elif userMood == "excited":
    print("That's awesome! What's the occasion?")
else:
    print("I'm sorry to hear that.")

"""
3. Personalized Greetings: 

Create a program where the chatbot asks for the user's name and the current time (morning, afternoon, evening). Depending on the time provided, the chatbot should greet the user with "Good morning, [name]!", "Good afternoon, [name]!", or "Good evening, [name]!".
"""
userName == input("What is your name? ")
currentTime == input("What time of day is it? (morning, afternoon, evening) ")

if currentTime == "morning":
    print("Good morning, " + userName + "!")
elif currentTime == "afternoon":
    print("Good afternoon, " + userName + "!")
else:
    print("Good evening, " + userName + "!")