def solve():
    s = input()
    odd = 0
    cnt = 0
    even = 0
    cnt1 = 0
    ok = 0
    i = 0
    for i in range(len(s)):

        if i % 2 == 0:
            if s[i] == "1":
                even += 1
            elif s[i] == "?":
                cnt += 1
        else:
            if s[i] == "1":
                odd += 1
            elif s[i] == "?":
                cnt1 += 1
        
        if odd + cnt1 > even + (9 - i) / 2:
            return i + 1
            ok = 1
        
        if even + cnt > odd + (10 - i) / 2:
            return i + 1
            ok = 1
    
    if not ok:
        return i + 1

for i in range(int(input())):
    print(solve())
