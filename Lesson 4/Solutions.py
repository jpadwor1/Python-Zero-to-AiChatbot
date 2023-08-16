"""
Homework 4:
Building More Interactivity for Our AI Chatbot:


1. While Loop Practice:

Write a program that simulates a countdown using a while loop. Start from a number provided by the user and countdown to zero.
"""
userNumber = int(input("Give me a number."))

while userNumber > 0:
    print(userNumber)
    userNumber -= 17
    
print("Done")
"""
2. For Loop with Indices:

Create a list of your favorite movies. Write a program that displays each movie with a number using a for loop with indices.
"""
favoriteMovies = ["The Shawshank Redemption", "Inception", "The Godfather", "Spirited Away", "The Matrix"]

for i, movie in enumerate(favoriteMovies):
    print(f"{i+1}: {movie}")


"""
3. Chatbot Task Completion:

Imagine the chatbot has a list of user questions. Use a for loop with indices to display each question with a number. Then, allow the user to select a question by its number to get a predefined answer.
"""

userQuestions = [
    "What is the capital of France?",
    "Who wrote the play 'Romeo and Juliet'?",
    "Which planet is known as the 'Red Planet'?",
    "Which element has the chemical symbol 'Au'?"
]


for i, question in enumerate(userQuestions):
    print(f"{i+1}: {question}")

userChoice = input("Here is a list of recommended questions, please select a question by entering the corresponding number.")


if userChoice == "1":
    print("Paris")
elif userChoice == "2":
    print("William Shakespeare")
elif userChoice == "3":
    print("Mars")
else:
    print("Gold")

