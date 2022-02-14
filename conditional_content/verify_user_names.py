current_users = ["ryan", "sheron", "someone", "nobody", "anybody", "alee"]

new_users = ["thomas", "jhon", "RYAN", "luke", "someone"]

for new_user in new_users:

    if new_user.lower() in current_users:
        print(f"The user name {new_user} is unavailable. Please select another.")

    else:
        print(f"{new_user} is available.")
