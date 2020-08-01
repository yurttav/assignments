#https://github.com/yurttav/assignments.git

line = " ".join('-'*15)
print(line)
for i in range(len(sudoku)):
    for j in range(len(sudoku[i])):
        if j % 3 == 0 and j != 0:
            print('| ', end = "")
        print(f"{sudoku[i][j]} ",end=" ")
    print()
    if (i+1) % 3 == 0:
        print(line)