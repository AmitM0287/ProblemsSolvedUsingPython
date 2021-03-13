"""
Q. Flip Coin and print percentage of Heads and Tails.
    a. I/P -> The number of times to Flip Coin. Ensure it is positive integer.
    b. Logic -> Use Random Function to get value between 0 and 1. If < 0.5 then tails or heads.
    c. O/P -> Percentage of Head vs Tails.
"""
from random import random
from logging_configuration import logging_config

logger = logging_config.get_logger()


def flip_coin(number_of_times_):
    """
    flip_coin(number_of_times_): This function count heads and tails after flip the coin number of times.
    It returns head count and tail count.
    """
    tail_count = 0
    # counting tails
    for number in range(number_of_times_):
        random_number = random()
        if random_number < 0.5:
            tail_count += 1
    # counting heads
    head_count = number_of_times_ - tail_count
    return head_count, tail_count


def calculate_percentage(head_count_, tail_count_):
    """
    calculate_percentage(head_count_, tail_count_): This function calculate Head and Tail percentage.
    It returns head percentage and tail percentage.
    """
    total_count = head_count_ + tail_count_
    # calculate head percentage
    head_percentage = round((head_count_ / total_count) * 100)
    # calculate tail percentage
    tail_percentage = 100 - head_percentage
    return head_percentage, tail_percentage


if __name__ == '__main__':
    try:
        number_of_times = int(input('Enter how many times you want to flip the coin : '))
        if number_of_times > 0:
            head_counts, tail_counts = flip_coin(number_of_times)
            percentage_of_head, percentage_of_tail = calculate_percentage(head_counts, tail_counts)
            print('Head Percentage is : ', percentage_of_head, '%')
            print('Tail Percentage is : ', percentage_of_tail, '%')
        else:
            print('Enter positive integers only! Please try again...')
    except ValueError:
        print('Enter integers only! Please try again...')
    except Exception as e:
        print('Oops! Something went wrong! Please try again...')
        logger.exception(e)
