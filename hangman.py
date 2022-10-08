word = input()
guesses = input()

components = 0
unique = list(set(word))

for l in guesses:
    if not (l in unique):
        components += 1
        if components == 10:
            print("LOSE")
            exit()
    else:
        unique.remove(l)
        if len(unique) == 0:
            print("WIN")
            exit()

