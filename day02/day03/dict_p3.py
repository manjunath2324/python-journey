d = {}
for i in range(4):
    name = input("Enter your name : ")
    language = input("Enter your fav language :")
    print("\n")
    d.update({name:language})

d1 = d.items()
print("Dictionary : ",d1)