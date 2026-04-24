x = input().strip()

if 'a' <= x <= 'z':
    print(chr(ord(x) - 32))
else:
    print(chr(ord(x) + 32))
    
    
