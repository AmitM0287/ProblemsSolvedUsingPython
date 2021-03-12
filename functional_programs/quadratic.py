# 4. Write a program to find the roots of the equation a*x*x + b*x + c.
#    Since the equation is x*x, hence there are 2 roots.
#    The 2 roots of the equation can be found using a formula (Note: Take a, b and c as input values)
#    delta = b*b - 4*a*c
#    Root 1 of x = (-b + sqrt(delta))/(2*a)
#    Root 2 of x = (-b - sqrt(delta))/(2*a)

from numpy import sqrt


# calculating roots
def calc_root(delta_, a_, b_):
    sqrt_delta = round(sqrt(delta_), 4)
    r1 = (-b_ + sqrt_delta) / (2 * a_)
    r2 = (-b_ - sqrt_delta) / (2 * a_)
    return round(r1, 4), round(r2, 4)


if __name__ == '__main__':
    try:
        print('General Expression of Quadratic Equation : ax^2 + bx + c = 0')
        # taking the value of a, b, c from the user to calculate the roots
        a = int(input('Enter the value of a : '))
        b = int(input('Enter the value of b : '))
        c = int(input('Enter the value of c : '))
        # calculate the delta value
        delta = b*b - 4*a*c
        # store the roots
        root1, root2 = calc_root(delta, a, b)
        # print the roots value
        print('Root 1 of x is : ', root1)
        print('Root 2 of x is : ', root2)
    except Exception as e:
        print(e)