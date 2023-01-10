numbers = []
count = 0
max_pare = 0

with open('17.txt') as file:
    for number in file:
        numbers.append(int(number))


for i in range(len(numbers) - 1):
    if numbers[i] % 3 == 0 or numbers[i + 1] % 3 == 0:
        count += 1
        if numbers[i] + numbers[i + 1] > max_pare:
            max_pare = numbers[i] + numbers[i + 1]

print(count)
print(max_pare)