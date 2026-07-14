numbers = []

for i in range(4):
    num = int(input(f"Enter number {i+1}:"))
    numbers.append(num)
print("Numbers :",numbers)    
a = numbers[0]
b = numbers[1]
c = numbers[2]
d = numbers[3]
if a>b and a>c and a>d:
    print(f"a: {a} is greater ")
elif b>c and b>d:
    print(f"b: {b} is greater")
elif c>d:
    print(f"c: {c} is greater")
else:
    print(f"d: {d} is greater")
    