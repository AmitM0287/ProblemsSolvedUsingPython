"""
Q. JSON Inventory Data Management of Rice, Pulses and Wheats
    Desc -> Create a JSON file having Inventory Details for Rice, Pulses and Wheats with properties name,
        weight, price per kg.
    I/P -> read in JSON File
    Logic -> Get JSON Object in Java or NSDictionary in iOS. Create Inventory Object from JSON.
        Calculate the value for every Inventory.
    O/P -> Create the JSON from Inventory Object and output the JSON String
"""
from logging_configuration import logging_config
from object_oriented_programs.inventory_data_management.InventoryDetails import InventoryDetails

logger = logging_config.get_logger()


if __name__ == '__main__':
    try:
        InventoryDetails().json_handler()
    except Exception as e:
        print('Oops! Something went wrong! Please try again!')
        logger.exception(e)
