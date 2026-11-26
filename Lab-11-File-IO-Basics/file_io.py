# Open a file in write mode
with open('output.txt', 'w') as file:
    # Write text to the file
    file.write('Hello, World!\n')
    file.write('This is a test of file I/O.\n')

# Open the file in append mode
with open('output.txt', 'a') as file:
    # Append text to the file
    file.write('Appending new text.\n')

# Open the file in read mode
with open('output.txt', 'r') as file:
    # Read content from the file
    content = file.read()
    # Print the content
    print(content)
