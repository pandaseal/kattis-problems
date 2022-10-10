tests = []

n = int(input())
while not n == 0:
    list1 = []
    list2 = []

    # pick up the lists
    for i in range(n):
        list1.append((int(input()), i)) # eg: [(48, 0), (10, 1), (97, 2)]
    for _ in range(n):
        list2.append(int(input())) # eg: [7, 46, 20]

    # sort list 1
    list1.sort(key=lambda tup: tup[0]) # eg: [(10, 1), (48, 0), (97, 2)]
    index = [i for (_, i) in list1] # eg: [1, 0, 2]

    # sort list 2 according to order of list 1
    list2.sort() # eg: [7, 20, 46]
    ziplist = zip(index, list2) # eg: [(1, 7), (0, 20), (2, 46)]
    list2_sorted = sorted(ziplist, key=lambda tup: tup[0]) # eg: [(0, 20), (1, 7), (2, 46)]

    # save list 2 for print
    tests.append([i for (_, i) in list2_sorted]) # eg: [20, 7, 46]

    # read next n
    n = int(input())

# print all 'list 2' with spaces between
for (i, test) in zip(range(len(tests)), tests):
    for j in test:
        print(j)
    if i < len(tests)-1:
        print()