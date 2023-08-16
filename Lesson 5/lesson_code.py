# A simple function to greet a user

def greet_user(name):
    return f"Hello, {name}! Welcome to our AI Chatbot journey."

# Using the function
user_name = input("What's your name? ")
print(greet_user(user_name))



def fetch_news():
    # For now, let's return a sample news headline
    return "Breaking: Python becomes the most popular programming language!"

def play_music():
    return "Playing: 'Journey to AI' by CodeTunes."

# Using our functions
print(fetch_news())
print(play_music())
