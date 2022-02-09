guests = ['Sheron', 'Ryan', 'Others']
for guest in guests:
    print(f'{guest}, would you like to have dinner with me?')

print("\nHey, I've found a bigger table.\n")

guests.insert(0, 'Anyone')
guests.insert(2, 'Someone')
guests.append('Nobody')

for guest in guests:
    print(f'{guest}, would you like to have dinner with me?')
