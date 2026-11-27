import subprocess

# Run the ls command and capture its output
result = subprocess.run(
    ['ls', '-l', 'demo'],
    capture_output=True,
    text=True
)

# Display standard output
print("Standard Output:")
print(result.stdout)

# Display standard error
print("Standard Error (if any):")
print(result.stderr)
