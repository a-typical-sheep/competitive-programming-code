for t in range(int(input())):
    n = input()
    l = len(n)

    if l > 10:
        array = []
        array.append(n[0])
        array.append(str(l - 2))
        array.append(n[l - 1])
        print("".join(array))
    else:
        print(n)