# 5. Harmonic Number
#    a. Desc -> Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N
#    b. I/P -> The Harmonic Value N. Ensure N != 0
#    c. Logic -> compute 1/1 + 1/2 + 1/3 + ... + 1/N
#    d. O/P -> Print the Nth Harmonic Value.

import logging

# implementing logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s : %(name)s : ', datefmt='%m/%d/%Y %I:%M:%S %p')
file_handler = logging.FileHandler('exceptions.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


# calculate Nth Harmonic Value
def harmonic_val(num):
    """harmonic_val(num): This function calculate the n-th harmonic value.
       It returns the n-th harmonic value of that integer."""
    res = 0
    for _ in range(1, num+1):
        res += 1/_
    return res


if __name__ == '__main__':
    try:
        N = int(input("Enter a integer to get it's Harmonic Value : "))
        # check weather N is a positive integer or not
        if N > 0:
            val = round(harmonic_val(N), 4)
            print('The Harmonic Value of ', N, ' is : ', val)
        else:
            print('Please enter a positive integer!')
    except Exception as e:
        logger.exception(e)
