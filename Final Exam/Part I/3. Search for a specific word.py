word = input("Enter word to search: ")

with open("students.txt", "r") as file:
    content = file.read()

if word in content:
    print("Word exists in the file.")
else:
    print("Word does not exist in the file.")
