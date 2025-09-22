# Chapter 7

# rental_car
rental_choice = input("What kind of rental car would you like? ").lower()
print(f"\nI will try to see if we have a {rental_choice.title()} in stock.")

# restaurant_seating
people = input("How many people will be dining today? ").lower()
people = int(people)
if people > 8:
    print(f"\nSorry, for a table of {people} people, you will need to wait.")
else:
    print("\nYour table is ready.")

# multiples_of_ten
number = input("Give me a number and I'll see if it's divisible by 10. ")
number = int(number)
if number % 10 == 0:
    print(f"\nYes, {number} is divisible by 10.")
else:
    print(f"\nNo, {number} is not divisible by 10.")

# pizza
toppings = []

while True:
    pizza_topping = input("\nWhat toppings would you like on your pizza? ")
    print("\nEnter 'quit' once you are finished with your order. ")

    if pizza_topping.lower() == "quit":
        break
    else:
        toppings.append(pizza_topping)
        print(f"\n{pizza_topping.title()} has been added to your order. ")

print(f"\nHere are your list of toppings: {', '.join(toppings)}")

# movie_tickets
price = input("Please enter your age. ")
price = int(price)

if price < 3:
    print("\nYou get free entrance! ")
elif (price >= 3 and price <= 12):
    print("\nYour ticket price is $10. ")
else:
    print("\nYour ticket price is $15. ")

# sandwiches
sandwiches_orders = ["bologna", "ham", "BLT", "turkey", "pastrami", "pastrami", "pastrami"]
finished_sandwiches = []

while "pastrami" in sandwiches_orders:
    sandwiches_orders.remove("pastrami")
    print("If you ordered pastrami, sorry, but we ran out today.")

while sandwiches_orders:
    current_order = sandwiches_orders.pop()
    print(f"Order up for {current_order.title()}.")
    finished_sandwiches.append(current_order)

print(f"\nThese are all the sandwiches we finished this shift:")
for finished_sandwich in finished_sandwiches:
    print(f"{finished_sandwich}")

# vacation
responses = {}
polling = True

while polling:
    name = input("What is your name? ")
    response = input("What is your dream vacation country? ")
    responses[name] = response

    repeat = input("Are there any other respondents? (type 'yes' or 'no') ")
    if repeat.lower == "yes":
        break
    elif repeat.lower() == "no":
        polling = False
        break
    else:
        print("Invalid answer. Type 'yes' or 'no'. ")

print("\nHere are the results:\n")
for name, response in responses.items():
    print(f"{name} would like to visit {response}.")






