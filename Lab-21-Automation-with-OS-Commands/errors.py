import subprocess
import sys

failed = 0

# 1. Handle a command that returns a non-zero exit code
try:
    subprocess.run(
        ['false'],
        check=True,
        capture_output=True,
        text=True
    )
except subprocess.CalledProcessError as e:
    print("Non-zero exit:", e.returncode)
    failed += 1

# 2. Handle a command that does not exist
try:
    subprocess.run(
        ['false_command'],
        check=True,
        capture_output=True,
        text=True
    )
except FileNotFoundError as e:
    print("Command not found:", e)
    failed += 1

# 3. Handle a command timeout
try:
    subprocess.run(['sleep', '5'], timeout=1)
except subprocess.TimeoutExpired as e:
    print("Timed out after", e.timeout, "second(s)")
    failed += 1

sys.exit(failed)
