import re
import sys

# Match phone numbers with balanced parentheses or plain area codes.
# Prevent matches inside longer digit strings.
phone_pattern = re.compile(
    r'(?<![\w(])(?:\(\d{3}\)|\d{3})[-.\s]?\d{3}[-.\s]?\d{4}(?!\d)'
)

def find_phone_numbers(file_name):
    with open(file_name, 'r') as file:
        text = file.read()
    return phone_pattern.findall(text)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 phone_finder.py FILE")
        sys.exit(1)

    matches = find_phone_numbers(sys.argv[1])

    if matches:
        print("Phone numbers found:")
        for match in matches:
            print(match)
    else:
        print("No phone numbers found.")
