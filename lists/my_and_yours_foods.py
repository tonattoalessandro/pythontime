my_foods = ['chocolate cake', 'chicken', 'pie']
friend_foods = my_foods[:]

my_foods.append('soup')
friend_foods.append('barbecue')

print("My favorite foods are:")
for food in my_foods:
    print(f"\t{food}")

print("\nMy friend favorite foods are:")
for food in friend_foods:
    print(f"\t{food}")
