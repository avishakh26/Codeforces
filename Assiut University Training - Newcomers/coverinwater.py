# t = int(input())

# for _ in range(t):
#     n = int(input())
#     s = input().strip()

#     i = 0
#     ans = 0

#     while i < n:
#         if s[i] == '#':
#             i += 1
#             continue

#         length = 0
#         while i < n and s[i] == '.':
#             length += 1
#             i += 1

#         if length <= 2:
#             ans += length
#         else:
#             ans += (length + 1) // 2

#     print(ans)



t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    i = 0
    ans = 0

    while i < n:
        if s[i] == '#':
            i += 1
            continue

        segment = ""
        while i < n and s[i] == '.':
            segment += s[i]
            i += 1

        if "..." in segment:
            ans += 2
        else:
            ans += len(segment)

    print(ans)