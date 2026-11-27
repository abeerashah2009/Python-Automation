import argparse
import csv
import logging
import sys

import requests

URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_posts():
    response = requests.get(URL, timeout=10)
    response.raise_for_status()
    return response.json()


def process_posts(data, user_id):
    processed = [{"userId": p["userId"], "title": p["title"]} for p in data]
    return [p for p in processed if p["userId"] == user_id]


def write_csv(rows, path="user_posts.csv"):
    with open(path, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["userId", "title"])
        writer.writeheader()
        writer.writerows(rows)


logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)


def get_data():
    try:
        data = fetch_posts()
        logging.info("Data fetched successfully (%d records)", len(data))
        return data
    except requests.exceptions.RequestException as e:
        logging.error("Error fetching data: %s", e)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Fetch and process API data")
    parser.add_argument("--user_id", type=int, default=1, help="User ID to filter posts by")
    args = parser.parse_args()

    rows = process_posts(get_data(), args.user_id)
    print(f"User {args.user_id} has {len(rows)} posts")
    write_csv(rows)
    logging.info("Wrote %d rows for user %d", len(rows), args.user_id)


if __name__ == "__main__":
    main()
