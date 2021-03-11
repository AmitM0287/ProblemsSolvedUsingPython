# 6. Factors
#   a. Desc -> Computes the prime factorization of N using brute force.
#   b. I/P -> Number to find the prime factors
#   c. Logic -> Traverse till i*i <= N instead of i <= N for efficiency.
#   d. O/P -> Print the prime factors of number N.

from math import sqrt


def prime_factors(num_):
    ls = []
    # Print the number of two's that divide n
    while num_ % 2 == 0:
        ls.append(2)
        num_ = num_ / 2
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(sqrt(num_)) + 1, 2):
        # while i divides n , print i ad divide n
        while num_ % i == 0:
            ls.append(i)
            num_ = num_ / i
    # Condition if n is a prime number greater than 2
    if num_ > 2:
        ls.append(int(num_))
    return ls


if __name__ == '__main__':
    try:
        num = int(input("Enter a number to get it's prime factors : "))
        if num > 0:
            factors = prime_factors(num)
            print('Prime factors of ', num, ' are : ', end='')
            for _num in factors:
                print(_num, ' ', end='')
        else:
            print('Please enter a positive integer')
    except Exception as e:
        print(e)
