a,b,c,d = (map(int,input().split()))

left = max(a,c)
right = max (b,d)

if left <= right:
    print(left,right)
    
else:
    print(-1)