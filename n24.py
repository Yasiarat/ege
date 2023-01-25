'''count = 1
max_count = 0

with open('24_demo.txt') as file:
    line = file.readline()

for i in range(len(line) - 1):
    if line[i] != line[i + 1]:
        count += 1
    else:
        max_count = max(max_count, count) # максимальное количество идущих подряд символов, среди которых каждые два соседних различны
        count = 1

print(max_count)'''

'''count = 0
#Определите количество строк, в которых буква A встречается чаще, чем буква E.
with open('no24.txt') as file:
    for line in file:
        if line.count('A') > line.count('E'):
            count += 1

print(count)'''

'''with open('2418.txt') as file:
    line = file.readline()
# Определите символ, который чаще всего встречается в файле сразу после буквы A.
m = 0
b = ''
for i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
    if m < line.count('A' + i):
        m = line.count('A' + i)
        b = i
print(m, b)'''

with open('2420.txt')as file:
    line = file.readline()

mk = 0
b = ''
d = {letter: 0 for letter in 'QWERTYUIOPASDFGHJKLZXCVBNM'}
#Определите символ, который чаще всего встречается в файле между двумя одинаковыми символами.
for i in range(1, len(line) - 1):
    if line[i - 1] == line[i + 1]:
        d[line[i]] += 1

max_value = 0
max_key = ''
for key, value in d.items():
    if value > max_value:
        max_key = key
        max_value = value

print(max_key, max_value)


#print(d[line[i]])
