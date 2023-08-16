# Let's say we have 5 cookies in our jar.
cookies_in_jar = 5

while cookies_in_jar > 0:
    print(f"Eating a cookie! {cookies_in_jar} cookies left.")
    cookies_in_jar -= 1

print("The cookie jar is empty!")


hobbies = ["reading", "sports", "music"]

for i, hobby in enumerate(hobbies):
    print(f"Hobby #{i+1}: {hobby}")


tasks = ["fetch news", "play music", "set alarm"]

for i, task in enumerate(tasks):
    print(f"Chatbot is now performing task #{i+1}: {task}.")
