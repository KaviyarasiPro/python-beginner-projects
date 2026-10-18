
print("Welcome to the Mad Libs Game!")

name = input("Enter a name: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")
food = input("Enter a food: ")
adjective = input("Enter an adjective: ")
verb = input("Enter an action verb: ")

story = f"""
One day, {name} went to {place}.
There, {name} saw a {adjective} {animal}.
The {animal} was eating {food}.
Suddenly, {name} started to {verb}.
It was an unforgettable day!
"""

print("\n--- Your Story ---")
print(story)

