"""
Homework 2:
Building More Interactivity for Our AI Chatbot:


1. Conveyor Belt of Colors:

Create a list of your favorite colors. Write a program that uses a loop to display each color with a message, e.g., "One of my favorite colors is [color]."
"""
favoriteColors = ["blue","red","green","purple","yellow"]

for color in favoriteColors:
    print(color)

"""
2. Chatbot Questionnaire:

Expand the chatbot interaction. After displaying each common question, allow the user to input an answer. Then, have the chatbot respond with a simple acknowledgment, e.g., "Got it!", after each answer.
"""
common_questions = ["How are you?", "What's your name?", "Do you like Python?"]

for question in common_questions:
    input(question)
    print("Got it!")


"""
3. Personalized Chatbot Responses:

Write a program where the chatbot asks the user for their favorite hobby.
Using if-else statements, have the chatbot respond with a personalized message based on a few predefined hobbies. For example:
If the user says "reading", the chatbot can respond with "Reading is a great way to expand the mind!"
If the user says "sports", the chatbot can say "Sports are a fantastic way to stay active and healthy!"
For any other hobby, the chatbot can respond with "That sounds interesting! Tell me more about it."
"""

favoriteHobby = input("What is your favorite hobby? Reading, sports, or something else? ")

if favoriteHobby == "sports":
    print("Sports are a fantastic was to stay active and healthy!")
elif favoriteHobby == "reading":
    print("Reading is a great way to expand the mind!")
else:
    print("That sounds interesting! Tell me more about it.")

