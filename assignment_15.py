def fizz_buzz(num):

    return ((((num % 3 == 0) or "") and "Fizz") + (((num % 5 == 0) or "") and "Buzz")) or num 

for i in range(1,101):

    print(i, fizz_buzz(i))