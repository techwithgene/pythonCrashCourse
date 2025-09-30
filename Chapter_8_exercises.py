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

# city names
def city_country(city, country):
    full_location = f"{city.title()}, {country.title()} "
    return full_location

while True:
    print("\nWhat is your location? Enter 'Quit' to exit program.")
    user_city = input("First, tell me your city. ")
    if user_city.lower() == "quit":
        break

    user_country = input("Next, tell me your country. ")
    if user_country.lower() == "quit":
        break

    formatted_location = city_country(user_city, user_country)
    print(f"Hello, your location is {formatted_location}.\n")

# album v1
# def make_album(artist, album, track_number=None):
#     album_detail = {"artist_name": artist, "album_name": album}
#     if track_number:
#         album_detail["track_number"] = track_number
#     return album_detail
#
# test1 = make_album("Me", "My", 5)
# test2 = make_album("Mo", "Ma")
# test3 = make_album("Mi", "Mu", 10)

# print(test1)
# print(test2)
# print(test3)

# album v2
def make_album(artist, album, track_number=None):
    album_detail = {"Artist Name": artist, "Album Name": album}
    if track_number:
        album_detail["track_number"] = track_number
    return album_detail

while True:
    artist = input("What is the name of the musical artist? ")
    if artist.lower() == "quit":
        break
    album = input("What is the title of the album? ")
    if album.lower() == "quit":
        break
    track_number = input("Do you know how many tracks are on the album? "
                         "If you don't know, press enter. ")
    if track_number.lower() == "quit":
        break

    user_album = make_album(artist, album, track_number)
    print("Here is the album info:", user_album)

# Messages
messages = ["Hello", "Goodbye", "Bye"]
delivered_messages = []
def send_messages(source_list, delivered_list):
    while messages:
        current_message = source_list.pop()
        print(f"the following message is being delivered: {current_message}")
        delivered_list.append(current_message)

send_messages(messages, delivered_messages)

print("The following messages have been delivered:\n")
print(delivered_messages)