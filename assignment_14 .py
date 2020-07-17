def is_prime(number):
    for i in range(2,number):
        if number % i == 0:
            return False
    return True

number = int(input("Please enter a number : "))
print([i for i in range(2,number+1) if is_prime(i)])