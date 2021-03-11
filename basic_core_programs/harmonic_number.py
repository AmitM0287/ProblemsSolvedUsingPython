# 5. Harmonic Number
#    a. Desc -> Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N
#    b. I/P -> The Harmonic Value N. Ensure N != 0
#    c. Logic -> compute 1/1 + 1/2 + 1/3 + ... + 1/N
#    d. O/P -> Print the Nth Harmonic Value.

# calculate Nth Harmonic Value
def harmonic_val(n):
    res = 0
    for i in range(1, n+1):
        res += 1/i
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
        print(e)
