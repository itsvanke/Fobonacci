num = int(input("Enter any Num: "))

is_prime = True

if num > 1:
    for i in range(2, int((num**0.5)+1)):
        if num % i == 0:
            is_prime = False
            break
else:
    is_prime = False

if is_prime:
    print("Given Number is a Prime Number")
else:
    print("Given Number is Not a Prime Number")