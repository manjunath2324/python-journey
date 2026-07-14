print("Enter six students marks:")
marks = []
for i in range(6):
    mark = int(input(f"marks of student {i+1}: "))
    marks.append(mark)
marks.sort()
print("Sorted marks are :",marks)