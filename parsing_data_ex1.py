first_chars = []
f = open('test.txt')
for line in f:
    first_chars = first_chars + [line[0]]
print(first_chars)
