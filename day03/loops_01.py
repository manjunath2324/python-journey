num = int(input("Enter a number : "))
for i in range(1,11):
    mult = num * i 
    print(f"{num} * {i} = {mult}")

for i in range(1,11):
    for j in range(1,11):
        m = i * j
        print(f"{i} * {j} = {m}")
    print()    