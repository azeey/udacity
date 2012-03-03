count=1
#count=15622
while True:
    n=[0]*7
    n[0] = count
    s = 0
    for i in range(1,7):
        if ((n[i-1] - 1) % 5) == 0:
            n[i] = 4*(n[i-1] - 1) / 5
            s += 1

    if s == 6:
        print count
        print n
        break
    else:
        count += 1
