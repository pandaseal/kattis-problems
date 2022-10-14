line = input()
a, b, c = line.split()
a = int(a)
b = int(b)
c = int(c)

if (a+b) == c: # add
    print("{}+{}={}".format(a,b,c))
elif a == (b+c):
    print("{}={}+{}".format(a,b,c))
elif (a-b) == c: # sub
    print("{}-{}={}".format(a,b,c))
elif a == (b-c):
    print("{}={}-{}".format(a,b,c))
elif (a*b) == c: # mult
    print("{}*{}={}".format(a,b,c))
elif a == (b*c):
    print("{}={}*{}".format(a,b,c))
elif (a/b) == c: # div
    print("{}/{}={}".format(a,b,c))
else:
    print("{}={}/{}".format(a,b,c))