# 2. Flip Coin and print percentage of Heads and Tails
#    a. I/P -> The number of times to Flip Coin. Ensure it is positive integer.
#    b. Logic -> Use Random Function to get value between 0 and 1. If < 0.5 then tails or heads
#    c. O/P -> Percentage of Head vs Tails

from random import random


#   Counting heads and tails
def flip_coin(num):
    c_tail = 0
    # Calculate tail count
    for _ in range(num):
        ran = random()
        if ran < 0.5:
            c_tail += 1
    # Calculate head count
    c_head = num - c_tail
    # Calculate head & tail percentage
    c_head, c_tail = cal_percent(c_head, c_tail)
    return c_head, c_tail


# Calculating Head and Tail - Percentage
def cal_percent(head_, tail_):
    total = head_ + tail_
    # Calculate head percentage
    h = round((head_/total)*100)
    # Calculate tail percentage
    t = 100 - h
    return h, t


if __name__ == '__main__':
    try:
        n = int(input('Enter how many times you want to flip the coin : '))
        if n > 0:
            per_head, per_tail = flip_coin(n)   # Flip the coin multiple times
            print('Head Percentage is : ', per_head, '%')
            print('Tail Percentage is : ', per_tail, '%')
        else:
            print('Please enter a positive integer!')
    except Exception as e:
        print(e)
