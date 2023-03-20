numList = input("Wprowadz liczby oddzielone przecinkiem (e.g. 1,5,4,2,1,6,7,12,51)\n")
numSplit = numList.split(",")
print(numSplit)
print(numSplit[0])
min = int(numSplit[0])
max = int(numSplit[0])
for i in numSplit:
    if int(i) < min:
        min = int(i)
    if int(i) > max:
        max = int(i)
print("Max: " + str(max) + " Min: " + str(min))