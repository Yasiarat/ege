from itertools import permutations
with open("1_24.txt") as file:
    s = file.readline()

last = 'K'
imposter = set([''.join(i) for i in permutations('AABBCC', 2)])
template = 0
mx = 0
print(imposter)

for i in s:
    if i + last not in imposter:
        template += 1
        mx = max(mx, template)
    else:
        template = 1
    last = i

print(mx, len(s))

