guests = ['Sheron', 'Ryan', 'Others', 'Anyone', 'Someone', 'Nobody']
for guest in guests:
    print(f'{guest}, would you like to have dinner with me?')

print("\nHey, friends, we won't have enough space to everybody. There are 2 places available only.")

uninvited = guests.pop(-1)
print(f"{uninvited}, I'm very sorry.")
uninvited = guests.pop(-1)
print(f"{uninvited}, I'm very sorry.")
uninvited = guests.pop(-1)
print(f"{uninvited}, I'm very sorry.")
uninvited = guests.pop(-1)
print(f"{uninvited}, I'm very sorry.")
print()

for guest in guests:
    print(f"{guest}, I still want you there.")

del guests[0]
del guests[0]

print()
print(guests)
