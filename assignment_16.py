#https://github.com/yurttav/assignments.git

year = int(input("enter a year please:"))

isleap = year%4==0 and not year%100==0 or year%400==0

print(f"{year} {isleap and 'is' or 'is not'} a leap year")