
t = int(input())

for _ in range(t):
    
    numbers = list(map(int, input().split()))
    
    
    possible_sums = []
    
    for i in range(7):
        current_sum = 0
        for j in range(7):
            if i == j:
                
                current_sum += numbers[j]
            else:
                
                current_sum += (numbers[j] * -1)
        
        possible_sums.append(current_sum)
    
    
    print(max(possible_sums))