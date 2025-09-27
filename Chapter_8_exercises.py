# Simple Greeting v1
# def greet_user():
#     user = input("What is your first name? ")
#     print(f"Hello {user.title()}, it's nice to meet you. ")
# greet_user()
# greet_user()

# Simple Greeting v2
def greet_username(username):
    print(f"Hello {username.title()}. ")
greet_username("fred")

# book
def favorite_book(book):
    print(f"{book.title()} is a great book. ")
favorite_book("The Hobbit")
favorite_book("Ender's Game")

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

def make_shirt(text, size="Large"):
    print(f"The front label will read: '{text}'")
    print(f"\nThe shirt size is {size}.\n")
make_shirt("This is a medium sized shirt.", "Medium")
make_shirt("This is a small sized shirt.", "Small")
# Same behavior
make_shirt(text="Large shirt")
make_shirt("Large shirt")

# city
def describe_city(city, country="America"):
    print(f"{city.title()} is a city in {country}")
describe_city(city="Newark")
describe_city(city="Los Angeles")
describe_city(city="London", country="England")

