word = input("Enter the string: ")
if "  " in word:
    print("The string contains double spaces.")
else:
    print("The string does not contain double spaces.")

m = word.replace("  ", " ")
print("The string after replacing double spaces with a single space is:", m)