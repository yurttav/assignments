#https://github.com/yurttav/assignments.git

def char_numbers(text):
    return {k:text.count(k) for k in set(text)}
print(char_numbers(input('Please enter a text: ')))