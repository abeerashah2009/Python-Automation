import subprocess

# Run a command using a path that does not exist
result = subprocess.run(
    ['ls', '/nonexistent'],
    capture_output=True,
    text=True
)

# Check the command exit code
if result.returncode == 0:
    print("Command executed successfully.")
else:
    print("Command failed with exit code:", result.returncode)
    print("stderr:", result.stderr.strip())
