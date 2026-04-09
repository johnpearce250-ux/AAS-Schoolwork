pets = [
    {"name": "Fido", "type": "dog"},
    {"name": "Whiskers", "type": "cat"},
    {"name": "Spot", "type": "dog"},
    {"name": "Goldie", "type": "fish"},
]
by_type={}

for pet in pets:
    name=pet['name']
    types=pet['type']

    current_list=by_type.get(types, [])
    current_list.append(name)
    by_type[types]=current_list

print(by_type)