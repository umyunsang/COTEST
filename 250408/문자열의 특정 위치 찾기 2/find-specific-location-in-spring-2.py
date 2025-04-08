words = ["apple", "banana", "grape", "blueberry", "orange"]
ch = input().strip()

result = []

for word in words:
    if len(word) >= 4:
        if word[2] == ch or word[3] == ch:
            result.append(word)

for word in result:
    print(word)

print(len(result))
