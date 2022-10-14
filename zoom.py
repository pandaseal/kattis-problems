n, k = input().split()
line = input().split()

s = ""
for j in [line[i-1] for i in range(int(n)+1) if i % int(k) == 0 and i > 0]:
    s += j + " "
print(s)    