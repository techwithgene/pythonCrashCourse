# 5-3/4/5/6
alien_color = 'green'
if alien_color == 'green':
    print('5 points for you')
else:
    print('no luck, no points')

alien_color = 'purple'
if alien_color == 'green':
    print('5 points for you')
else:
    print('10 points!')

alien_color = 'red'
if alien_color == 'green':
    print('5 points for you')
elif alien_color == 'yellow':
    print('10 points for yellow')
else:
    print('15 points for red!')

age = 66
if age < 2:
    print('Baby')
elif age < 4:
    print('toddler')
elif age < 13:
    print('teenager')
elif age < 20:
    print('adult')
elif age >= 65:
    print('elder')

# book version
my_favorite_fruits = ['apple', 'tomato', 'banana']
if 'apple' in my_favorite_fruits:
    print("Wow I love apples!")
if 'orange' in my_favorite_fruits:
    print("Wow I love oranges!")
if 'banana' in my_favorite_fruits:
    print("Wow I love bananas!")
if 'tomato' in my_favorite_fruits:
    print("Wow I love tomatoes!")
if 'berry' in my_favorite_fruits:
    print("Wow I love berries!")

# my version
my_favorite_fruits = ['apple', 'orange', 'banana']
user_fruit = input('What is your favorite fruit?\n').lower()

if user_fruit in my_favorite_fruits:
    print(f'Me too, I would love an {user_fruit}.')
else:
    print("I don't like that fruit.")

#usernames = ['admin', 'abe', 'bac', 'cad', 'dae']
usernames = []
if not usernames:
    print("No users found.")
else:
    for username in usernames:
        if username == 'admin':
            print("Hello master.")
        else:
            print(f'Welcome {username}!')

current_users = ['admin', 'abe', 'bac', 'cad', 'dae']
new_users = ['admin', 'abe', 'bac', 'cad', 'eke']
for new_user in new_users:
    if new_user in current_users:
        print(f"Sorry, but {new_user} is already a current username.")
    else:
        print("That is a valid new username.")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")