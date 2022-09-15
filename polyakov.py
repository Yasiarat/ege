'''import itertools

s = 'ПРЕПАРАТ'

p = itertools.permutations(s)  # все перестановки строк

p = set(p)  # убрать дубликаты

print(len(p))'''




count = 0
for a in 'Е':
    for b in 'ЕГЭИНФ':
        for c in 'ЕГЭИНФ':
            for d in 'ЕГЭИНФ':
                for e in 'ЕГЭИНФ':
                    for f in 'ЭИ':
                        s = a + b + c + d + e + f
                        if s.count('ФИ') == 2 and s.count('ЕГЭ') == 0:
                            count += 1
print(count)