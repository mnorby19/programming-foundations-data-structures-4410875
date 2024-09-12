def has_unique_characters(data):
    information = set(data)
    return len(data) == len(information)

print(has_unique_characters('sample'))
print(has_unique_characters('hello world'))
print(has_unique_characters('linkedin'))
print(has_unique_characters('python'))
