t = int(input())

for _ in range(t):
    n = list(map(int, input().split()))

    even = 0
    odd = 0
    pos = 0
    neg = 0

    for x in n:
        if x % 2 == 0:
            even += 1
        else:
            odd += 1

        if x > 0:
            pos += 1
        elif x < 0:
            neg += 1

    print("Even:", even)
    print("Odd:", odd)
    print("Positive:", pos)
    print("Negative:", neg)
    
    
    