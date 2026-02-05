with open("students.txt", "r") as file:
    lines = file.readlines()

total_lines = len(lines)
total_words = sum(len(line.split()) for line in lines)

print("Total lines:", total_lines)
print("Total words:", total_words)
