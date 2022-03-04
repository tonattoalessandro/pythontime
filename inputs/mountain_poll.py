from timeit import repeat
from urllib import response


responses = {}

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like climb someday? ")

    responses[name] = response
    
