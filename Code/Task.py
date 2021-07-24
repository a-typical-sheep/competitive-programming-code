import re

def count_substring(string, sub_string):
    return len(re.findall('(?='+sub_string+')',string))

N, Q = map(int, input().split())

S = input()

for q in range(Q):
    type, L, R, W = input().split()
    type = int(type)
    L = int(L)
    R = int(R)

    if type == 1:
        print(count_substring(S[L - 1:R], W))
    else:
        arr = list(S)
        arr2 = list(W)
        for i in range(L - 1, R):
            arr.pop(i)
        for i in arr2:
            arr.insert(L, i)
        arr = map(str, arr)
        S = "".join(arr)