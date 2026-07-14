m = []
total = 0
max_marks = 100
for i in range(3):
    marks = int(input(f"marks of subject {i+1} :"))
    m.append(marks)
total = sum(m)
for i in range(len(m)):
    p = (m[i]/max_marks)*100
    print("Individual subjects percentage :",p)
print("Total marks are :",total)
percentage = (total/300)*100
print(" total percentage is ",percentage)
print(m)