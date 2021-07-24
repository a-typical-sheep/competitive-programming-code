for i in range(int(input())):
    n, x, t = map(int, input().split())
    f1 = min(t/x, n)
    print(1 * f1 * (f1 - 1)/2 + 1 * (n - f1) * f1)