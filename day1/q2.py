f = open("q2-input.txt", "r")
col1, col2 = [], []
for i in f:
    line = i.split(" ")
    col1.append(line[0])
    col2.append(line[-1].rstrip())

res = []
for i in col1:
    multiplier = 0
    for j in col2:
        if i == j:
            multiplier += 1
    res.append(int(i) * multiplier)

print(sum(res))
