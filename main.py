def task27424():
    with open("27-B_demo.txt", "r", encoding="utf-8") as f:
        n, *pairs = f.readlines()

    pairs: list[str]

    mx_list, mn_list = [], []
    mn_diff = 10000000

    for s in pairs:
        pair = sorted(map(int, s.strip().split()))
        mn_list.append(pair[0])
        mx_list.append(pair[1])
        if (pair[1] - pair[0]) % 3 != 0:
            mn_diff = min(mn_diff, pair[1] - pair[0])

    print(sum(mx_list) - mn_diff)
    print((sum(mx_list) - mn_diff) % 3)
    print(mn_diff)



