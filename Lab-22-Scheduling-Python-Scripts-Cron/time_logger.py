# time_logger.py
import datetime
from pathlib import Path

LOG_FILE = Path.home() / "cron_lab" / "log.txt"

def log_time():
    with open(LOG_FILE, "a") as file:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"Current Time: {current_time}\n")

if __name__ == "__main__":
    log_time()
