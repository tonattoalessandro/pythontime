favorite_places = {
    'joe': ['Paris', 'London', 'Orlando',],
    'jack': ['Florida'],
    'john': ['Iceland', 'Finland',],
}

for person, places in favorite_places.items():
    print(f"\n{person.title()} favorite places are:")
    for place in places:
        print(f"\t{place}")
