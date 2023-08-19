"""
Homework for Video 1.5:
Building Blocks for Our AI Chatbot:



1. Grocery Bill Calculator:

You went shopping and bought a few items. Write a program that calculates your total bill.

Ask the user for the price of three items.
Calculate the total price of the items.
Print out the total cost.
"""
item1_price = int(input("Enter the price of the first item: "))
item2_price = int(input("Enter the price of the second item: "))
item3_price = int(input("Enter the price of the third item: "))

total_cost = item1_price + item2_price + item3_price

print(f"Total cost: ${total_cost}")


"""  
2. Savings Account:

Imagine you have a savings account and you want to know how much you'll have after depositing a certain amount every month.

Ask the user for their current savings.
Ask the user how much they plan to deposit every month.
Calculate the total savings after 6 months of deposits.
Print out the total savings.
"""
current_savings = int(input("Enter your current savings: "))
monthly_deposit = int(input("Enter your monthly deposit: "))

total_savings = current_savings + (monthly_deposit * 6)

print(f"Total savings after 6 months: ${total_savings}")


"""
3. Grade Percentage Calculator:

You just took a test and want to know your percentage score.

Ask the user for the total number of questions on the test.
Ask the user how many questions they answered correctly.
Calculate the percentage of correct answers.
Print out the percentage score.
"""

test_questions = int(input("Enter the total number of questions: "))
correct_questions = int(input("Enter the number of questions you answered correctly: "))

score = (correct_questions // test_questions) * 100

print(f"Your score is {score}%.")


"""
4. Splitting the Bill:

You went out to eat with friends and need to split the bill.

Ask the user for the total bill amount.
Ask the user how many people are splitting the bill.
Calculate how much each person should pay.
Print out the amount each person should pay.
"""

total_bill = int(input("Enter the total bill amount: $"))
number_people_splitting = int(input("Enter the number of people: "))

share_price = total_bill / number_people_splitting

print(f"Each person should pay: ${share_price}")





