L = int(input()) # between 1 and 10k
D = int(input()) # same
X = int(input()) # 1 <= X <= 36

# N : minimal digit N so that L <= N <= D AND sum of digits in N is X
# M : maximal digit M so that L <= M <= D AND sum of digits in M is X

for N in range(L, D+1):
    sum = 0
    for i in str(N):
        sum += int(i)
    if sum == X:
        print(N)
        break

for M in range(D, L-1, -1):
    sum = 0
    for i in str(M):
        sum += int(i)
    if sum == X:
        print(M)
        break