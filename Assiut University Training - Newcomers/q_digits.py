N = int(input())

for _ in range(N):
    n = input()
    
    for digit in n[::-1]:
        print(digit, end=' ')
    print()
    
    