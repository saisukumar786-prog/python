s = input("Enter text: ")
s = s.lower()
filtered = ''
for c in s:
    if c.isalnum():
        filtered += c
if filtered == ''.join(reversed(filtered)):
    print("Palindrome")
else:
    print("Not a palindrome")
