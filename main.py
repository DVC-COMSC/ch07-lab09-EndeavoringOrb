names = list(input().split(" "))
names_sorted = []
for i in range(len(names)):
    names_sorted.insert(0,names[i])
    if len(names_sorted[i]) > len(names_sorted[i+1]):
        names_sorted[i],names_sorted[i+1] = names_sorted[i+1],names_sorted[i]
    elif len(names_sorted[i]) == len(names_sorted[i+1]):
        if ord(names_sorted[i][0]) > ord(names_sorted[i][0]):
            names_sorted[i],names_sorted[i+1] = names_sorted[i+1],names_sorted[i]
print(names[0])
print(names[len(names)-1])