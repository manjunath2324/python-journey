marks = int(input("Enter marks :"))
if marks >90 and marks <= 100:
    print("The student got Ex Grade")
elif marks > 80 and marks <= 90:
    print("A Grade")
elif marks > 70 and marks <= 80:
    print("B Grade")
elif marks >60 and marks <= 70:
    print("C Grade")
elif marks >50 and marks <= 60:
    print("D Grade")
else:
    print("F Grade") 