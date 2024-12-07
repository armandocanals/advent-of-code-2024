f = open("q1-testinput.txt", "r")
res = []
reports = 0
for i in f:
    line = i.split(" ")
    line[-1] = line[-1].replace("\n", "")
    direction = ""
    reports += 1
    for idx in range(len(line) - 1):
        distance = abs(int(line[idx]) - int(line[idx + 1]))
        if distance > 3:
            res.append("unsafe")
            break
        elif distance <= 0:
            res.append("unsafe")
            break
        elif int(line[idx]) > int(line[idx + 1]):
            if direction and direction == "increasing":
                res.append("unsafe")
                break
            direction = "decreasing"
        elif int(line[idx]) < int(line[idx + 1]):
            if direction and direction == "decreasing":
                res.append("unsafe")
                break
            direction = "increasing"

print(res)
print(reports - len(res))
