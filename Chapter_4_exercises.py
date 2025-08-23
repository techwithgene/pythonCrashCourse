# 4-1 Pizzas For Loops
pizzas = ['pepperoni', 'plain', 'supreme']
for pizza in pizzas:
    print(f'{pizza.title()} is one of my favorites!')
    print(f'We should order a {pizza.lower()} pizza together!\n')

# 2 versions of output
pizzas_list = ', '.join(pizzas)
print(f'Basically, I love {pizzas_list} pizzas. Yay for pizza lovers!')
print(f'Basically, I love {pizzas[0]}, {pizzas[1]}, and {pizzas[2]} pizzas. Yay for pizza lovers!')


