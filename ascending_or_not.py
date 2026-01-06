num = int(input("Enter a number: "))
ascending = True
prev_digit = num % 10   
num //= 10             
while num > 0:
    curr_digit = num % 10
    if curr_digit > prev_digit:   
        ascending = False
        break
    prev_digit = curr_digit
    num //= 10
if ascending:
    print("Ascending order")
else:
    print("Not Ascending order")