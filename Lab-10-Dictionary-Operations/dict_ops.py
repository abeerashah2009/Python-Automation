# Task 1: Creating a dictionary with person information
person_info = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

print("Created:", person_info)

# Task 2: Retrieving the value for key 'name'
name_value = person_info['name']
print("Name:", name_value)

# Task 3: Updating an existing dictionary value
person_info['age'] = 31

# Adding a new key-value pair
person_info['occupation'] = 'Engineer'

# Display the updated dictionary
print("Updated Dictionary:", person_info)

# Verification
assert person_info['age'] == 31 and 'occupation' in person_info
print("Checks passed")
