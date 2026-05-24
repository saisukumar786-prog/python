text = input("Enter a string: ")
target = input("Enter the character to count: ")
count = 0

for ch in text:
    if ch == target:
        count += 1

print(f"The character '{target}' appears {count} time(s) in the string.")
