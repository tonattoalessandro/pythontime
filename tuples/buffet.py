from dis import dis


dishes = ('pasta', 'cake', 'pie', 'meat', 'chicken')
print("Original MENU:")
for dish in dishes:
    print(f"\t{dish}")

dishes = ('pasta', 'lasagna', 'pie', 'meat', 'bacon and eggs')
print("\nModified MENU:")
for dish in dishes:
    print(f"\t{dish}")
