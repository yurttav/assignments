number = int(input("Please enter a number : "))
isprime = ""
for i in range(2,number):
    if number % i == 0:
        isprime = " not"
        break
print(f"{number} is{isprime} a prime number")