# Chapter 3-1
names = ['kyle', 'mike', 'dave']
print(f'Hi {names[0].title()}!')
print(f'Hi {names[1].title()}!')
print(f'Hi {names[2]}!')

#Chapter 3-2
guests = ['abe lincoln', 'Lee Kew Yuan', 'Nikola Tesla']
print(f'Hi {guests[0].title()}, what is it like being president?')
print(f'Hi {guests[1].title()}, what is it like being prime minister?')
print(f'Hi {guests[2].title()}, what is it like being a scientist?')

print('Whoops, look like Abe cannot make it.')
guests.remove('Abe Lincoln'.lower())

guests.append('Albert Einstein')
guests.sort()

print(f'The new guest list is {guests}')
