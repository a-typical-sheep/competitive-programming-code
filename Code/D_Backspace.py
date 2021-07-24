for i in range(int(input())):
    s = input()
    t = input()

    s = s[::-1]
    t = t[::-1]

    index1 = 0

    i = 0
    while i < len(s):
        if index1 == len(t):
            break
        if s[i]  == t[index1]:
            index1 += 1
        else:
            i += 1
        i += 1

    if index1 == len(t):
        print("YES")
    else:
        print("NO")