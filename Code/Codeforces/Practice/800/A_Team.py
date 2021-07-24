solution = 0
for i in range(int(input())):
    x, y, z = map(int, input().split())

    if (x == 0 and y == 0) or (x == 0 and z == 0) or (y == 0 and z == 0):
        continue
    else:
        solution += 1

print(solution)
