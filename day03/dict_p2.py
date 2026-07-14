numbers = set()
print("Enter eight numbers :")
for i in range(8):
    num = int(input(f"number {i+1}:"))
    numbers.add(num)

print("unique numbers :",numbers)
