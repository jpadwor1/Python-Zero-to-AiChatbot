"""
Homework for Video 7: Logical Operators in Python

**Remember the logical operators only work with boolean values. So, if you take user input as a string then that will need to be converted to a boolean

1. Movie Night Decision:

You and your friends are trying to decide if you should go out for a movie. Write a program that helps you decide based on the following conditions:

You will go if it's a weekend OR if there's a special weekday discount.
However, if it's raining AND you don't have an umbrella, you won't go, regardless of the other conditions.
"""


is_weekend = True
is_discount = False
is_raining = True  
has_umbrella = False

if (is_weekend or is_discount) and not (is_raining and has_umbrella):
    print("Decision: Have a great night out!")
else:
    print("Decision: Better stay at home.")



"""
2. Fitness Class Signup:

A fitness class has specific signup requirements. Write a program that checks if a person can sign up based on the following:

The person can sign up if they are 18 or older AND the class is not full.
If the person is younger than 18, they can still sign up if they have parental consent OR if there's a special youth program running.
"""
age = int(input("Enter your age: "))

class_capacity = input("Is the class full? (true/false): ")
consent = input("Do you have parental consent? (true/false): ")
youth_program = input("Is there a special youth program? (true/false): ")

if class_capacity == "false":
    if age >= 18:
        print("You can sign up for the fitness class!")
    elif age < 18 and (consent == "true" or youth_program == "true"):
        print("You can sign up for the fitness class!")
    else:
        print("Sorry you cannot attend the class.")
else:
    print("Sorry, the class is full.")



"""
3.  Library Membership System:

You're developing a system for a local library. Write a program that determines if a user can borrow a book based on the following:

The user can borrow a book if they have a valid library card AND no overdue books.
If the user is a premium member, they can borrow a book even if they have overdue books, but they still need to have a valid library card.

"""

library_card = input("Do you have a valid library card? (true/false): ")
overdue_books = input("Do you have any overdue books? (true/false): ")
premium_membership = input("Are you a premium member? (true/false): ")

if library_card == "true" and (overdue_books == "false" or premium_membership == "true"):
    print("You can borrow a book!")
else:
    print("Sorry we cannot allow you to borrow a book!")



