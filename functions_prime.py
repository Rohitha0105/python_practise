def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def next_prime(num):
    next_num = num + 1
    while True:
        if is_prime(next_num):
            return next_num
        next_num += 1

def prev_prime(num):
    prev_num = num - 1
    while prev_num > 1:
        if is_prime(prev_num):
            return prev_num
        prev_num -= 1
    return None 

def nearest_prime(num):
    next_p = next_prime(num)
    prev_p = prev_prime(num)

    print(next_p, "is the next prime number")
    if prev_p:
        print(prev_p, "is the previous prime number")

    a = num - prev_p if prev_p else float('inf')
    b = next_p - num

    if a > b:
        print("Next prime is nearest")
    elif a == b:
        print("Both are nearest")
    else:
        print("Previous prime is nearest")

num = int(input("Enter a number: "))
nearest_prime(num)