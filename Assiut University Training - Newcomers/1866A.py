
n = int(input())
arr = list(map(int, input().split()))



if 0 in arr:
    print(0)
else:
    
    min_op = min(abs(x) for x in arr)
    print(min_op)
    
    