x, y = 0, 1
fibo = []

while y < 56:
    fibo.append(y)
    x, y = y, x+y

print(fibo)