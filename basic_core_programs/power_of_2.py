# 3. Power of 2
#    a. Desc -> This program takes a command-line argument N and prints
#       a table of the powers of 2 that are less than or equal to 2^N.
#    b. I/P -> The Power Value N. Only works if 0 <= N < 31 since 2^31 overflows an int.
#    c. Logic -> repeat until i equals N.

from sys import argv


# Calculating power of 2 until i == N
def power_of(n):
    k = 0
    ls = []
    while k != n:
        ls.append(2**k)
        k += 1
    return ls


if __name__ == '__main__':
    try:
        N = int(argv[1])
        # validating the given condition
        if 0 <= N < 31:
            data = power_of(N)
            for val in data:
                print(val, ' ', end='')
        else:
            print('Please enter a integer(N) between 0 <= N <31 this range!')
    except Exception as e:
        print(e)
