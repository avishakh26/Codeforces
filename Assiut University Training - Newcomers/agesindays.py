N = int(input())

years = N // 365

remaining = N % 365
 
months = remaining // 30

days = remaining % 30


print(years,"years")
print(months,"months")
print(days,"days")