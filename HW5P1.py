'''
Homework 5 Part 1 - coding
Maher Harkati
Problem 1 - Data Warehousing
'''

import random
import string
from collections import defaultdict

class DataWarehouse:
    def __init__(self):
        self.data_collector = []
        self.key_value_pairs = defaultdict(list)

    def generate_random_string(self, length=8):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    def generate_user_data(self, num_users=100):
        cities = ['Springfield', 'Rivertown', 'Lakeview', 'Pineville', 'Maplewood']  # List of cities
        states = ['CA', 'NY', 'TX', 'FL', 'IL']  # List of states
        streets = ['Main', 'Maple', 'Oak', 'Cedar', 'Elm']  # List of street names
        salespersons = ['John', 'Jane', 'Bob', 'Alice', 'Eve']  # List of salespersons

        for _ in range(num_users):
            user_data = {
                'username': self.generate_random_string(),
                'password': self.generate_random_string(),
                'birthdate': f"{random.randint(1950, 2000)}-{random.randint(1, 12)}-{random.randint(1, 28)}",
                'address': f"{random.randint(100, 999)} {random.choice(streets)} St, {random.choice(cities)}, {random.choice(states)}",
                'ssn': f"{random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(1000, 9999)}",
                'productPurchased': {
                    'orderID': f"ID-{self.generate_random_string()}",
                    'webOrder': random.choice([True, False]),
                    'productID': f"ID-{self.generate_random_string()}",
                    'quantity': random.randint(1, 10),
                    'dateOfOrder': f"{random.randint(2020, 2023)}-{random.randint(1, 12)}-{random.randint(1, 28)}",
                    'region': self.generate_random_string()
                },
                'salesperson': f"SalesID-{random.choice(salespersons)}"
            }
            self.data_collector.append(user_data)

    def create_key_value_pairs(self):
        for idx, user_data in enumerate(self.data_collector):
            user_id = f"UserID-{idx + 1}"
            self.key_value_pairs[user_id] = user_data

    def search_users(self, key, value):
        result = []
        for user_id, user_data in self.key_value_pairs.items():
            if key in user_data and user_data[key] == value:
                result.append((user_id, user_data))
            elif isinstance(user_data.get(key), dict):
                nested_dict = user_data[key]
                if any(value in nested_value for nested_value in nested_dict.values()):
                    result.append((user_id, user_data))
        return result



def main():
    # Example Usage
    warehouse = DataWarehouse()

    # Step One: Generate User Data
    warehouse.generate_user_data()

    # Step Two: Create Key/Value Pairs
    warehouse.create_key_value_pairs()

    # Step Three: Search for users in a certain state (address)
    state_search_result = warehouse.search_users('address', '500 Maple St, Springfield, IL')  # Change the street name, city, and state as needed
    print("Users in a certain state:")
    for user_id, user_data in state_search_result:
        print(f"{user_id}: {user_data}")

    # Search for users handled by a certain salesperson
    salesperson_search_result = warehouse.search_users('salesperson', 'SalesID-Bob')  # Change the salesperson as needed
    print("\nUsers handled by a certain salesperson:")
    for user_id, user_data in salesperson_search_result:
        print(f"{user_id}: {user_data}")

main()
