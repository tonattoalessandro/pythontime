guests = ['Sheron', 'Ryan', 'Others']
for guest in guests:
    print(f'{guest}, would you like to have dinner with me?')
absent = 'Others'
guests.remove('Others')
print(f'{absent} is unavailable today.')
guests.append('Someone')
print()
for guest in guests:
    print(f'{guest}, would you like to have dinner with me?')
