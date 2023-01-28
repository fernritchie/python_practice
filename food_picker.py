import random

# List of food types
food_type = ["Chinese", "Pizza", "Fish & Chips", "Stir fry"]

# Functoion to pick a random food type
def yummy_food():
    num = random.randint(0, 3)
    winning_dish = food_type[num]
    print("The winner is..." + winning_dish)

# Prompt for user input
option_list = int(input("Hi there, please choose an option"))

# Loop through options 1 to 3
for i in range(0,option_list):
    print('Enter 1\n')
    print('Enter 2\n')
    print('Enter 3\n')
    choice = int(input('Enter your choice:'))
    if (choice == 1):
        yummy_food()

    elif (choice == 2):
        add_yummy_food = str(input("What food would you like to add?"))
        food_type = food_type + add_yummy_food
        print("You now have..." + food_type)

    else:
        print("NAH")
            
