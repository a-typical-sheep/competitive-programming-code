def cyclic(l, i):
    return l[n:] + l[:n]

for i in range(int(input())):
    n, m = map(int, input().split())
    t = list(map(int, input().split()))

    p = [int(i) for i in range(1, n + 1)]
    print(p)