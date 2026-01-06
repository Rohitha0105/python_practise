num = int(input())
even = 0
odd = 0
while num > 0:
    dig = num % 10
    if dig % 2 == 0:
        even += dig
    else:
        odd += dig 
    num = num // 10
print(even)
print(odd)