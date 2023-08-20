"""
Homework for Video 8:

Dice Simulator:

Task: Create a program that simulates the roll of a dice.
Details: When executed, the program should display a random number between 1 and 6. Think of it as a virtual dice roll. Test it multiple times to see the randomness in action.
"""
import random

dice_roll = random.randint(1, 6)

print(f"Roll: {dice_roll}")


"""
Lucky Draw:

Task: Design a program that conducts a lucky draw.
Details: Start with a list of names (at least 5). The program should randomly select one name as the winner and display it. Consider adding a drum roll effect using a pause before revealing the winner!
"""
import time
names = ["John", "Aaron", "Erica", "Kip", "Eric", "Sally"]

winner = random.choice(names)

print("Drum Roll Please")
print("././././././././")
time.sleep(2)
print(f"The winner is {winner}")

"""
Random Password Generator:

Task: Develop a random password generator.
Details: The password should be 8 characters long and include a mix of uppercase letters, lowercase letters, numbers, and at least one special character. Challenge yourself: Can you ensure every password generated meets these criteria?
"""
lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


special_characters = ['!', '@', '#', '$', '%', '&']

password = [random.choice(special_characters)]# Ensure it has at least 1 special character

for i in range(8): # ensure password is sufficient length
    password.append(random.choice(lowercase_letters + uppercase_letters + digits + special_characters))

#shuffle the password for extra randomness
random.shuffle(password)

random_password = ''.join(password)

print(random_password)



"""
Shuffle Playlist:

Task: Shuffle your music playlist.
Details: Create a list of 10 of your favorite songs. The program should shuffle and display them in a new order each time it's run. Compare the different orders each time!
"""

songs = [
    "Bohemian Rhapsody by Queen",
    "Imagine by John Lennon",
    "Billie Jean by Michael Jackson",
    "Shape of You by Ed Sheeran",
    "Like a Rolling Stone by Bob Dylan",
    "Purple Rain by Prince",
    "Smells Like Teen Spirit by Nirvana",
    "Stairway to Heaven by Led Zeppelin",
    "Rolling in the Deep by Adele",
    "Despacito by Luis Fonsi ft. Daddy Yankee"
]

random.shuffle(songs)
print(songs)


"""
Random Math Quiz:

Task: Design a mini math quiz.
Details: The program should randomly generate a simple arithmetic problem, like adding two random numbers between 1 and 10. After the user answers, tell them if they're correct or not.
"""
operators = ["+", "-", "*", "//"]  # Use integer division to ensure an integer result

random_operator = random.choice(operators)

first_int = random.randint(1, 10)
second_int = random.randint(1, 10)

def math(operator, first_int, second_int):
    if operator == "+":
        user_answer = int(input(f"{first_int} + {second_int} = "))
        answer = first_int + second_int
    elif operator == "-":
        user_answer = int(input(f"{first_int} - {second_int} = "))
        answer = first_int - second_int
    elif operator == "//":
        while second_int == 0:  # Ensure we're not dividing by zero
            second_int = random.randint(1, 10)
        user_answer = int(input(f"{first_int} // {second_int} = "))
        answer = first_int // second_int
    else:
        user_answer = int(input(f"{first_int} * {second_int} = "))
        answer = first_int * second_int

    if answer == user_answer:
        print("Correct!")
    else:
        print(f"Sorry, that is incorrect. The correct answer is {answer}.")

math(random_operator, first_int, second_int)