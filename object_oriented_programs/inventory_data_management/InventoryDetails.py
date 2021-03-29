import json


class InventoryDetails:
    def __init__(self):
        self.name = []
        self.weight = []
        self.price_per_kg = []
        self.total = []

    def json_handler(self):
        """
        This function is used to handle the json file.
        :return: None
        """
        with open('inventory_details.json', 'r') as json_file:
            data = json.load(json_file)
        # Getting the details from json and calculate total.
        for details in data['inventory_details']:
            self.name.append(details['name'])
            self.weight.append(details['weight'])
            self.price_per_kg.append(details['price_per_kg'])
            self.total.append(str(int(details['weight']) * int(details['price_per_kg'])))
        # Assigned the total into the json file.
        index = 0
        for details in data['inventory_details']:
            details['name'] = self.name[index]
            details['weight'] = self.weight[index]
            details['price_per_kg'] = self.price_per_kg[index]
            details['total'] = self.total[index]
            index += 1
        with open("inventory_details.json", "w") as json_file:
            json.dump(data, json_file, indent=2)
