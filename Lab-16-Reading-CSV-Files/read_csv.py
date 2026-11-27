import csv

# Read CSV file
with open('sample.csv', mode='r', newline='') as file:
    csv_reader = csv.reader(file)

    # Skip header row
    next(csv_reader)

    # Display each record
    for row in csv_reader:
        print(f'Name: {row[0]}, Age: {row[1]}, Occupation: {row[2]}')

# TASK 4 - Summarize CSV data
total_age = 0
row_count = 0

with open('sample.csv', mode='r', newline='') as file:
    for row in csv.DictReader(file):
        total_age += int(row['Age'])
        row_count += 1

print(f'Total number of entries: {row_count}')
print(f'Total age combined: {total_age}')

if row_count > 0:
    print(f'Average age: {total_age / row_count:.2f}')
else:
    print('No records found.')
