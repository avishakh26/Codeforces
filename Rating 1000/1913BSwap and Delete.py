t = int(input())
for _ in range(t):
    s = input()
    cnt0 = s.count('0')
    cnt1 = s.count('1')
    print(abs(s.count('0') - s.count('1')))
    