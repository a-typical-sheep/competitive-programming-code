def solve():
    s, t = input().split()
    n = len(s)

    for i in range(n):
        if s[i] == t[0]:
            len1 = 0
            ptr = i
            ptr_t = 0
        
        while ptr < len(s) and ptr_t < len(t) and s[ptr] == t[ptr_t]:
            ptr += 1
            ptr_t += 1
            len1 += 1
        
        if len1 == len(t):
            return "YES"
    return "NO"

for i in range(int(input())):
    print(solve())