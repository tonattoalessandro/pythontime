user_names = ['ryan', 'sheron', 'alee', 'someone', 'admin']

if user_names:
    for user_name in user_names:
        if user_name == 'admin':
            print(f"Hello, {user_name}. Do you want to see a status report?")
        else:
            print(f"Hello, {user_name}.")

else:
    print("We need to find some users...")
