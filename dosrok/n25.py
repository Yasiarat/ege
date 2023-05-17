from fnmatch import fnmatch

for i in range(1200162, 10**8, 317):
    if fnmatch(str(i), '12??1*56'):
        print(i, i // 317)
        