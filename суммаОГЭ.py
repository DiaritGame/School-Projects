N = int(input())
S = 0
for i in range(N):
    x = int(input())
    if x % 6 == 0 and x % 10 == 8:
        S = S + x
print(S)