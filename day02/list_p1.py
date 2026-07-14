print("Enter  seven fruits names:")
fruits = []
for i in range(7):
    fruit = input(f"Fruit name {i+1}:")
    fruits.append(fruit)
# l.sort() and sorted(l) are used to sort the list but l.sort() does not return a new list it changes the original list and returns None,
#  wheres sorted(l) returns a new list and does not changes the original list.
fruits.sort()
print("Fruits names are : ",fruits)
