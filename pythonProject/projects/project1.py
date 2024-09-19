import random

user_input1 = int(input("Enter the lower bound: "))
user_input2 = int(input("Enter the upper bound: "))

rand = random.randint(user_input1, user_input2)
print(rand)