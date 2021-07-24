def solve():
    s = input()
    t = input()
    n = len(s)

    i = 0
    while i < n:
        if s[i] == t[0]:
            len1 = 0
            powert = i
            powert_t = 0
        
            while powert < len(s) and powert_t < len(t) and s[powert] == t[powert_t]:
                powert += 1
                powert_t += 1
                len1 += 1
            
            powert -= 2

            while powert >= 0 and powert_t < len(t) and s[powert] == t[powert_t]:
                powert -= 1
                powert_t += 1
                len1 += 1
            
            if len1 == len(t):
                return "YES"
        
        i += 1

    return "NO"

for i in range(int(input())):
    print(solve())