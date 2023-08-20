import random #By importing random, we now have access to all its functions, which allow us to generate random numbers, shuffle lists, and more.


# This will give us a random float between 0 and 1
random_float = random.random()
print(f"Random Float: {random_float}")

#But what if we want a random integer within a range? Say, between 1 and 10?
random_integer = random.randint(1, 10)
print(f"Random Integer between 1 and 10: {random_integer}")


#Imagine you're indecisive about which fruit to eat today. Let Python decide for you!
fruits = ["apple", "banana", "cherry", "date"]
chosen_fruit = random.choice(fruits)
print(f"Today's fruit choice is: {chosen_fruit}")


#Randomness can also help us mix things up. Let's shuffle our fruit list.
print("Original List:", fruits)
random.shuffle(fruits)
print("Shuffled List:", fruits)
