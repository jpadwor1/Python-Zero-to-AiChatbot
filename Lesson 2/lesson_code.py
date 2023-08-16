# Let's use our traffic light colors to make decisions.

traffic_light = "red"

if traffic_light == "red":
    print("Stop!")
elif traffic_light == "yellow":
    print("Slow down!")
else:
    print("Go!")

# Let's tie this back to our AI Chatbot. Imagine the chatbot asks a
# user for their mood. Depending on the response, the chatbot can
# reply differently.

userMood = input("How are you feeling today? ")

if userMood == "happy":
    print("That's great to hear!")
elif userMood == "sad":
    print("I'm here to help. Let's chat!")
else:
    print("Thanks for sharing your feelings.")
