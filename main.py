names = list(input().split(" "))
for i in range(len(names)-1):
    if len(names[i]) > len(names[i+1]):
        names[i],names[i+1] = names[i+1],names[i]
    elif len(names[i]) == len(names[i+1]):
        if ord(names[i][0]) > ord(names[i][0]):
            names[i],names[i+1] = names[i+1],names[i]
for i in range(len(names)):
    names[i][0].upper()
print(names[0])
print(names[len(names)-1])