f = open("input.txt", "r")
col1, col2 = [], []
for i in f:
    line = i.split(" ")
    col1.append(line[0])
    col2.append(line[-1].rstrip())

col1.sort(), col2.sort()
distances = []

for j in range(len(col1)):
    distances.append(abs(int(col1[j]) - int(col2[j])))

print(sum(distances))
