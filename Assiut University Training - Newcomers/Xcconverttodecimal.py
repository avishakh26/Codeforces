t = int(input())

for _ in range(t):
    n = int(input())

    count = 0

    while n > 0:
        if n & 1:
            count += 1
            
        n >>= 1  #shift operator newly learn

    print((1 << count) - 1)