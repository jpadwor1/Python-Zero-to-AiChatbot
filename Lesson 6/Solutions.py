"""
Homework 6:
Building More Interactivity for Our AI Chatbot:


1. List Manipulation:

Create a list of your top 3 favorite colors. 
Add two more colors to the list and then remove the first color. 
Print the updated list.
"""
favorite_colors = ["red","green","blue"]

favorite_colors.append("purple")
favorite_colors.append("black")
favorite_colors.append("yellow")
favorite_colors.remove(favorite_colors[0])
print(favorite_colors)



"""
2. List Length:

Create a list of five animals. Write a program that prints a message telling the user how many animals are in the list.
"""
animals = ["dog","cat","cow","horse","chicken"]

number_of_animals = 0

for animal in animals:
    number_of_animals +=1

print(f"There are {number_of_animals} animals in the list")

"""
3. Chatbot Song Queue:

Imagine the chatbot can queue up to three songs for a user. Allow the user to add songs to the list until there are three songs in the queue. Once the queue is full, display the list of songs to the user.
"""

song_queue = []

def make_queue():
    while len(song_queue) < 3:
        user_choice = input("Give me a song.")
        song_queue.append(user_choice)
    print(f"Your song list is \n {song_queue}")
make_queue()