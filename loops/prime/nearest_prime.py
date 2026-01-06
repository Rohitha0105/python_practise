num = int(input())
next_num = num
prev_num = num
next_prime_not_found = True
while next_prime_not_found == True:
    next_num +=1
    factor = 0
    for i in range(2,num):
        if next_num % i == 0:
            factor += 1
            break
    if factor == 0:
        next_prime_not_found = False
        print(next_num,"is a next prime number")
prev_prime_not_found = True
while prev_prime_not_found == True:
    prev_num -=1
    factor = 0
    for i in range(2,prev_num):
        if prev_num % i == 0:
            factor += 1
            break
    if factor == 0:
        prev_prime_not_found = False
        print(prev_num,"is a previous prime number")
a = num - prev_num
b = next_num - num
if a > b:
    print("Next prime is nearest")
elif a == b:
    print("Both are nearest")
else:
    print("previous is nearest")