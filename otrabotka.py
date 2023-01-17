'''
numbers = []
count = 0
max_pare = 0

with open('17 (1).txt') as file:
    for i in file:
        numbers.append(int(i))

for j in range(len(numbers) - 1):
    if (numbers[j] + numbers[j + 1]) % 2 == 1 and numbers[j] * numbers[j + 1] % 5 == 0:
        count += 1
        if numbers[j] + numbers[j + 1] > max_pare:
            max_pare = numbers[j] + numbers[j + 1]

print(count)
print(max_pare)
'''


count = 0
max_pare = 0

with open('17 (4).txt') as file:
    numbers = [int(i) for i in file]

for i in range(len(numbers) - 1):
    for j in range(i + 1, len(numbers)):
        if (numbers[i] - numbers[j]) % 2 == 0 and (numbers[i] % 31 == 0 or numbers[j] % 31 == 0):
            count += 1
            max_pare = max(max_pare, numbers[i] + numbers[j])

print(count, max_pare)
