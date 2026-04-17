A,B = map(int,input().split())

if B % A == 0 or A % B == 0:
    print("Multiples")
    
else:
    print("No Multiples")