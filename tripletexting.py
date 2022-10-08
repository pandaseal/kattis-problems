line = input()

length = int(len(line)/3)

w1 = line[0:length]
w2 = line[length:2*length]
w3 = line[2*length:]

if w1 == w2:
    print(w1)
elif w2 == w3:
    print(w2)
else:
    print(w3)