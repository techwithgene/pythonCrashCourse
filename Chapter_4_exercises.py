# 4-1 Pizzas For Loops
pizzas = ['pepperoni', 'plain', 'supreme', 'anchovy', 'meat']
for pizza in pizzas:
    print(f'{pizza.title()} is one of my favorites!')
    print(f'We should order a {pizza.lower()} pizza together!\n')

# 2 versions of output
pizzas_list = ', '.join(pizzas)
print(f'Basically, I love {pizzas_list} pizzas. Yay for pizza lovers!')
print(f'Basically, I love {pizzas[0]}, {pizzas[1]}, and {pizzas[2]} pizzas. Yay for pizza lovers!')

new_pizzas = pizzas[:4]
new_pizzas_list = ', '.join(new_pizzas)
print(f'the first 4 items in the list are {new_pizzas_list} and {pizzas[4]}.\n')

# 4-2 Animals for loops
animals = ['jaguar', 'cheetah', 'leopard']
for animal in animals:
    print(f'A {animal} is a spotted big cat.\n')
print(f'A {animals[0]}, {animals[1]}, and {animals[2]} are all spotted big cats.\n')

# 4-3/4/5/6 numbers and ranges
numbers = list(range(1, 21))
print(numbers)

error_number = list(range(1, 1_000_001))
#print(error_number)
print(min(error_number))
print(max(error_number))
print(sum(error_number))

numbers = list(range(1, 21, 2))
print(numbers)
numbers = list(range(3, 30, 3))
print(numbers)

cubes = []
for value in range(1, 16):
    cubes.append(value**3)
print(cubes)

cube = [value**3 for value in range(1, 11)]
print(cube)

