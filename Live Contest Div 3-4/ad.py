# t = int(input())

# for _ in range(t):
#     n = int(input())
    
#     ans = [1]
    
#     for i in range(1, n):
#         ans.append(i * (i + 1))
    
#     print(*ans)




import math

t = int(input())

for _ in range(t):
    n = int(input())
    
    a = [1]
    
    for i in range(1, n):
        a.append(i * (i + 1))
    
    print(*a)