prompt = "Enter the client age or 'quit' to end the program: "

while True:
    age = input(prompt)
    if age.lower() == 'quit':
        break
    age = int(age)
    if age < 3:
        print("Ticket is FREE!")
    elif age >= 3 and age < 12:
        print("Ticket - $10")
    else:
        print("Ticket - $15")
