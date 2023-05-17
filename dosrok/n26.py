with open("1_26.txt") as f:
    n = [[int(i) for i in line.split()] for line in f]
    box = n[0][0]
    del n[0:2]

n.sort()
print(n)

bitebox = [0] * box
winner = 0
mx = 0
ind = 0

for i in n:
    for j in bitebox:
        if i[0] > j:
            if i[0] >= mx:
                mx = i[0]
                ind = bitebox.index(j) + 1
            winner += 1
            bitebox[bitebox.index(j)] = i[1]
            break

print(winner, ind)
print(bitebox)
