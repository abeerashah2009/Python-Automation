from datetime import datetime, timedelta, timezone

# TASK 1 - Get current local date and time
current_datetime = datetime.now()
print("Current date and time:", current_datetime)

# Get current UTC date and time
utc_datetime = datetime.now(timezone.utc)
print("Current UTC date and time:", utc_datetime)

# TASK 2 - Calculate yesterday and next week's date
fixed = datetime(2026, 1, 15, 10, 30)

yesterday = fixed - timedelta(days=1)
next_week = fixed + timedelta(weeks=1)

print("Yesterday's date:", yesterday)
print("Next week's date:", next_week)

# Verify date calculations
assert yesterday.day == 14
assert next_week.day == 22
print("Assertions passed")

# TASK 3 - Format date and time
formatted_datetime = fixed.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date and time:", formatted_datetime)

# Verify formatted result
assert formatted_datetime == "2026-01-15 10:30:00"
print("Formatting assertion passed")
