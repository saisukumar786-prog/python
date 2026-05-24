from keyword import iskeyword

strings = ["hello print", "find world", "in language", "programming not in", "language count"]

keywords = []
for text in strings:
    for word in text.split():
        if iskeyword(word):
            keywords.append(word)

print("Original list:")
print(strings)
print("\nKeywords found:")
print(keywords)


