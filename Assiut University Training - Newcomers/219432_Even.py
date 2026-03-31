n = int(input())

found = False

for i in range(2, n + 1, 2):
    print(i)
    found = True

if not found:
    print(-1)