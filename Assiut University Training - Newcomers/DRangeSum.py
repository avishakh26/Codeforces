t = int(input())

for _ in range(t):
    L, R = map(int, input().split())
    
    if L > R:
        L, R = R, L
    
    sum_R = R * (R + 1) // 2
    sum_L = (L - 1) * L // 2
    
    print(sum_R - sum_L)
    
    
    