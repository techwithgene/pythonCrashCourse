# Chapter 6
friend = {
    "first_name": "Mike",
    "last_name": "Lee",
    "age": 35,
    "city": "East Brunswick"
}

print(friend["first_name"])
print(friend["last_name"])
print(friend["age"])
print(friend["city"])
print()
print(f"His first name = {friend['first_name'].title()}, "
      f"last name = {friend['last_name'].title()}, "
      f"his age = {friend['age']}, "
      f"and his city is {friend['city'].title()}.")

dictionary = {
    "tuple": "immutable/unchangeable list of elements using []",
    "list": "mutable/changeable list of elements using []",
    "dictionary": "Key: Value pair using {}",
    "nest": "'nested' within another statement or dictionary/list"
}

for word in dictionary.keys():
    print(f"\n{word.title()} - {dictionary[word]}")

rivers = {
    "nile": "africa",
    "amazon": "south america",
    "mississippi": "north america",
}

for river in rivers.keys():
    print(f"\nThe {river.title()} runs through {rivers[river]}\n")

for river in rivers.keys():
    print(f"{river.title()}")
print()
for river in rivers.values():
    print(f"{river.title()}\n")

languages = {
    "Abe": "Python",
    "Bae": "C+",
    "Cae": "Rust",
    "Dae": "Java"
}

students = ["Abe", "Eaj", "Cae"]

for student in students:
    if student in languages.keys():
        print(f"Thank you {student.title()} for voting.")
    else:
        print(f"{student.title()}, please vote for a language.")

people = {
    "mike": {
        "first_name": "Mike",
        "last_name": "Lee",
        "age": 35,
        "city": "East Brunswick",
    },
    "dan": {
        "first_name": "Dan",
        "last_name": "Crow",
        "age": 25,
        "city": "Howell",
    },
    "john": {
        "first_name": "John",
        "last_name": "Son",
        "age": 30,
        "city": "Marlboro",
    }
}

for friend, information in people.items():
    print(information["first_name"])
    print(information["last_name"])
    print(information["age"])
    print(information["city"])
    print()
    print(f"His first name = {information["first_name"].title()}, "
          f"last name = {information['last_name'].title()}, "
          f"his age = {information['age']}, "
          f"and his city is {information['city'].title()}.")

# pets = {
#     "Bud": {
#         "owner": "John",
#         "breed": "Corgi",
#         "age": "5"
#     },
#     "Doge": {
#         "owner": "Dan",
#         "breed": "Shiba Inu",
#         "age": "3"
#     },
#     "Kaiser": {
#         "owner": "Mike",
#         "breed": "German Shepard",
#         "age": "7",
#     }
# }

Bud = {
        "owner": "John",
        "breed": "Corgi",
        "name": "Bud",
        "age": "5"
    }
Doge = {
        "owner": "Dan",
        "name": "Doge",
        "breed": "Shiba Inu",
        "age": "3"
    }
Kaiser = {
        "owner": "Mike",
        "name": "Kaiser",
        "breed": "German Shepard",
        "age": "7",
    }
pets = [Bud, Doge, Kaiser]

for pet in pets:
    print(f"\nInformation for all the pets:\n{pet["name"]}")
    for key, value in pet.items():
        print(f"{key.title()}: {value}")

