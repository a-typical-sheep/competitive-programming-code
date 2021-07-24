m, n = map(int, input().split())

n = n * m
m = m * n

solution= 0
while (m >= 2 and n >= 1) or (m >= 1 and n >= 2):
    if max(m, n) == m:
        solution += 1
        m = m - 2
        n = n - 1
    else:
        solution += 1
        n = n - 2
        m = m - 1

print(solution)