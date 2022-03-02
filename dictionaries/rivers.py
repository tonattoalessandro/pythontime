rivers = {
    'nile': 'egypt', 'amazon': 'brazil', 'volga': 'russia',
}

for river, country in rivers.items():
    print(f"The {river.capitalize()} flows through {country.capitalize()}.")

print(f"\nThe rivers are:")
for river in rivers.keys():
    print(f"\t{river.title()}")

print(f"\nAnd the countries are:")
for country in rivers.values():
    print(f"\t{country.title()}")
