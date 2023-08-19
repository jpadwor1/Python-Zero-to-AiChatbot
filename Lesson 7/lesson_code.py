#The and operator checks if both conditions are True.

age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive!")
else:
    print("Sorry, you cannot drive.")


#The or operator checks if at least one condition is True.
is_weekend = True
has_free_time = False

if is_weekend or has_free_time:
    print("Let's go to the movies!")
else:
    print("Maybe another time.")

#The not operator reverses the result. If the result was True, it becomes False and vice versa
is_raining = False

if not is_raining:
    print("Let's go for a walk!")
else:
    print("Better stay indoors.")

#You can combine these operators for more complex conditions.

is_holiday = True
has_homework = False

if (is_weekend or is_holiday) and not has_homework:
    print("Time for a vacation!")
else:
    print("Regular day.")
