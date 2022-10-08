names = list(input().split(" "))
shortest = ""
longest = ""
for i in range(len(names)):
    if len(names[i]) < len(shortest):
        shortest = names[i]
    if len(names[i]) == len(shortest):
        if ord(names[i][0]) < len(shortest[0]):
            shortest = names[i]
    if len(names[i]) > len(longest):
        longest = names[i]
print(shortest)
print(longest)