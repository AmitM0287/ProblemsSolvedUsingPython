# 1. 2D Array
#    a. Desc -> A library for reading in 2D arrays of integers, doubles, or booleans from standard input
#       and printing them out to standard output.
#    b. I/P -> M rows, N Cols, and M * N inputs for 2D Array.
#    c. Logic -> create 2 dimensional array in memory to read in M rows and N cols
#    d. O/P -> Print function to print 2 Dimensional Array.

from numpy import zeros


# taking datatype from the user
def get_datatype():
    print('Please choose a datatype : \n 1. Integer \n 2. Float \n 3. Boolean \n You choose : ')
    ip = int(input())
    datatype = ''
    if ip == 1:
        datatype = 'int'
    elif ip == 2:
        datatype = 'float'
    elif ip == 3:
        datatype = 'bool'
    else:
        print('You chosen wrong input!')
        exit()
    return datatype


if __name__ == '__main__':
    try:
        row = int(input('Enter Row number : '))
        col = int(input('Enter Column number : '))
        arr = zeros((row, col), get_datatype())
        # Taking inputs from user
        for i in range(row):
            for j in range(col):
                print('Enter value for (', i, ',', j, ') position : ', end='')
                arr[i][j] = input()
        # Print the array
        print('Your 2D array is : ')
        for i in range(row):
            for j in range(col):
                print(arr[i][j], ' ', end='')
            print()
    except Exception as e:
        print(e)
