'''print('x', 'y', 'z', 'w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((x or not y) and (not (y == z)) and not w)
                if f == 1:
                    print(x, y, z, w)

'''
flag = True
'''for A in range(10000):
    for x in range(100):
        for y in range(100):
            f = ((x >= 12) or (3 * x < y) or (x * y < A))
            if f == 0:
                flag = False
                break
        if flag == False:
            flag = True
            break

    else:
        print(A)
        break
'''

'''
def f(n):
    if n >= 2025:
        return n
    return n + f(n + 2)

#print(f(2022) - f(2023))


def red(s):
    while ('25' in s) or ('335' in s) or ('555' in s):
        if '25' in s:
            s = s.replace('25', '5', 1)
        if '355' in s:
            s = s.replace('355', '52', 1)
        if '555' in s:
            s = s.replace('555', '3', 1)
    return s


for n in range(4, 1000):
    s = '2' + '5' * n
    d = 0
    l = red(s)
    for j in l:
        d += int(j)
    if d == 17:
        print(n)
        break
'''

def f(x, y):
    if x > y or x == 15:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x * 2, y) + f(x * 3, y)

print(f(1, 11) * f(11, 25))





























