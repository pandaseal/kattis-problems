# descr: https://open.kattis.com/problems/t9spelling

n = int(input())

msgs = [] # messages
seqs = [] # sequences
lookup = {}

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 0]
letters = ["abc","def","ghi","jkl","mno","pqrs", "tuv", "wxyz"," "]
keypad = zip(letters, numbers) # eg: [("abc", 2), ("def", 3), ...]

# build lookup table for letters
# lookup = {
#     "a": "2",
#     "b": "22",
#     ...
# }
for (letters, number) in keypad:
    for (letter, times) in zip(letters, range(len(letters))):
        seq = ""
        for _ in range(times+1):
            seq += str(number)
        lookup[letter] = seq

for i in range(n):

    # pick up the messages
    msg = input()

    # lookup sequences
    seq = ""
    last_key = "x"
    for l in msg:
        key = lookup[l]

        # add pause
        if key[0] == last_key[0]:
            seq += " "
        
        # add sequence
        seq += key
        last_key = key

    # save sequence
    seqs.append(seq)

# print cases
for i in range(n):
    print("Case #{}: {}".format(i+1, seqs[i]))