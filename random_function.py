import random
fruits = ["apple", "banana", "grapes", "avocado"]

random_num = random.randint(20,40)
print("random number generated", random_num)

random_fruit = random.choice(fruits)
print("random fruit picked", random_fruit)