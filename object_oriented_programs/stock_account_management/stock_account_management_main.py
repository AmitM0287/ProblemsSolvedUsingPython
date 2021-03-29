"""
Stock Account Management
    Desc -> Write a program to read in Stock Names, Number of Share, Share Price. Print a Stock
        Report with total value of each Stock and the total value of Stock.
    I/P -> N number of Stocks, for Each Stock Read In the Share Name, Number of Share, and Share Price
    Logic -> Calculate the value of each stock and the total value
    O/P -> Print the Stock Report.
"""
from logging_configuration import logging_config
from object_oriented_programs.stock_account_management.StockDetails import StockDetails

logger = logging_config.get_logger()


if __name__ == '__main__':
    try:
        StockDetails().json_handler()
    except Exception as e:
        print('Oops! Something went wrong! Try again...')
        logger.exception(e)
