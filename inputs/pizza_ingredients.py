prompt = ("Enter an ingredient for your pizza or 'quit' to end the program: ")

while True:
    ingredient = input(prompt)
    if ingredient.lower() == 'quit':
        break
    print(f"\t{ingredient.capitalize()} added to the pizza.")
