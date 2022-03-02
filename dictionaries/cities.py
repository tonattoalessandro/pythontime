cities = {
    'são paulo': {'country': 'brazil', 'population': 12330000, 'fact': 'it is the biggest city in the country',},
    'london': {'country': 'england', 'population': 8982000, 'fact': 'it is a cold city',},
    'milan': {'country': 'italy', 'population': 1352000, 'fact': 'the fashion city',},
}

for city, data in cities.items():
    print(f"\nCity: {city.title()}")
    country = data['country']
    population = data['population']
    fact = data['fact']
    print(f"\tCountry: {country.title()}")
    print(f"\tPopulation: {population} of people")
    print(f"\tA fact about {city.title()}: {fact.capitalize()}")
