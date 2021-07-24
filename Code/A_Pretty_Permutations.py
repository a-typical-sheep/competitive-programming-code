for i in range(int(input())):
    n = int(input())

    mylist = list(range(1, n + 1))

    mylist = [mylist[-1]] + mylist[:-1]

    print(" ".join(list(map(str,mylist))))