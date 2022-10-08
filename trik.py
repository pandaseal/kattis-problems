moves = input()

one = True
two = False
three = False

for m in moves:
    if m == "A":
        if not three:
            one = not one
            two = not two
    elif m == "B":
        if not one:
            two = not two
            three = not three
    else: # m == "C"
        if not two:
            one = not one
            three = not three

if one:
    print(1)
elif two:
    print(2)
else:
    print(3)
