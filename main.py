names = list(input().split(" "))
shortest = ""
longest = ""
print(names)
for i in range(len(names)):
    if len(names[i]) < len(shortest) or shortest == "":
        shortest = names[i]
    if len(names[i]) == len(shortest):
        if ord(names[i][0]) < ord(shortest[0]):
            shortest = names[i]
    if len(names[i]) > len(longest):
        longest = names[i]
    if len(names[i]) == len(longest):
        if ord(names[i][0]) > ord(longest[0]):
            longest = names[i]
print(shortest)
print(longest)