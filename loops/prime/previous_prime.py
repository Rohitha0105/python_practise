num = 17
prime_not_found = True
while prime_not_found == True:
    num -=1
    factor = 0
    for i in range(2,num):
        if num % i == 0:
            factor += 1
            break
    if factor == 0:
        prime_not_found = False
        print(num,"is a previous prime number")