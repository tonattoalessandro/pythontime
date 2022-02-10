my_pizzas = ['pepperoni', 'cheese', 'meat']
friend_pizzas = my_pizzas[:]

my_pizzas.append('hawaiian')
friend_pizzas.append('veggie')

print('My favorite pizzas are:')
for pizza in my_pizzas:
    print(f"\t{pizza}")

print("\nMy friend favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"\t{pizza}")
