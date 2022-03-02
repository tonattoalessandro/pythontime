pets = {
    'rex': {'sort': 'mouse', 'owner': 'joe',},
    'moon': {'sort': 'dog', 'owner': 'chloe',},
    'ted': {'sort': 'cat', 'owner': 'mike',},
    'jake': {'sort': 'parrot', 'owner': 'luke',},
}

for animal, data in pets.items():
    print(f"\n{animal.title()}")
    owner = data['owner'].title()
    sort = data['sort']

    print(f"\tOwner: {owner}\n\tSort: {sort}")
