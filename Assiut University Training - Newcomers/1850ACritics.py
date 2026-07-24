# n = int(input())

# for _ in range(n):
#     a,b,c = map(int,input().split())

#     if a + b >= 10 or a + c >= 10 or c + b >= 10:
        
#         print("YES")
#     else:
#         print("NO")
        
        
        
arr = list(map(int,input().split()))

found = False

for i in range(3):
    for j in range(i, 1+3):
        if arr[i] + arr[[j]] >= 10:
            found = True
            break
    if found:
        break 

if found:
    ("YES")
else:
    ("NO")
        