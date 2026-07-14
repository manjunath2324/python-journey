names = []
for i in range(5):
    name = input(f"Enter name of {i+1} person :")
    names.append(name)
name_to_find = input("Enter the name of the person you want to find :")
if name_to_find in names:
    print("The name you entered is present ")
else:
    print("The name you entered is not present in the list")