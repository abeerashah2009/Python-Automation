import csv

# Data represented as a list of dictionaries
data_dict = [
    {"Name": "Alice", "Age": 28, "City": "New York"},
    {"Name": "Bob", "Age": 34, "City": "Chicago"},
    {"Name": "Charlie", "Age": 22, "City": "San Francisco"}
]

# Data represented as a list of tuples
data_tuple = [
    ("Name", "Age", "City"),
    ("Alice", 28, "New York"),
    ("Bob", 34, "Chicago"),
    ("Charlie", 22, "San Francisco")
]

# Write CSV using csv.writer
with open('people.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for row in data_tuple:
        writer.writerow(row)

# Write CSV using csv.DictWriter
with open('people_dict.csv', 'w', newline='') as file:
    fieldnames = ["Name", "Age", "City"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for row in data_dict:
        writer.writerow(row)
