n, k = map(int, input().split())
participants = list(map(int, input().split()))

kscore = participants[k - 1]
solution = 0
participants.sort()

for i in participants:
    if i >= kscore and i > 0:
        solution += 1

print(solution)