

import csv

def load_passenger_data(file_path):
    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.DictReader(file)
            passengers = list(csv_reader)
            return passengers
    except FileNotFoundError:
        print(f"⚠️ Error: The file at {file_path} could not be found.")
        return []