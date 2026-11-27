import argparse
import logging
import time
from pathlib import Path

LAB_DIR = Path.home() / "FileCleanupLab"

logging.basicConfig(filename=str(LAB_DIR / "cleanup_log.txt"), level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")


def cleanup_old_files(directory, days_threshold, apply=False):
    seconds_threshold = days_threshold * 24 * 60 * 60
    current_time = time.time()
    count = 0
    for path in sorted(directory.iterdir()):
        if not path.is_file():
            continue
        age = current_time - path.stat().st_mtime
        if age > seconds_threshold:
            if apply:
                path.unlink()
                logging.info(f"Deleted: {path}")
                print(f"Deleted: {path}")
            else:
                logging.info(f"Dry run, would delete: {path}")
                print(f"Would delete: {path}")
            count += 1
    return count


def main():
    parser = argparse.ArgumentParser(description="Delete files older than N days.")
    parser.add_argument("directory", help="directory to clean (must be inside ~/FileCleanupLab)")
    parser.add_argument("days", type=int, help="delete files older than this many days")
    parser.add_argument("--apply", action="store_true",
                        help="really delete files (default is a dry run)")
    args = parser.parse_args()

    directory = Path(args.directory).resolve()
    if not directory.is_dir() or not directory.is_relative_to(LAB_DIR.resolve()) or directory == LAB_DIR.resolve():
        parser.error(f"refusing to use {directory}: must be a subdirectory of {LAB_DIR}")

    count = cleanup_old_files(directory, args.days, args.apply)
    verb = "deleted" if args.apply else "would be deleted (dry run)"
    print(f"Total files {verb}: {count}")
    logging.info(f"Total files {verb}: {count}")


if __name__ == "__main__":
    main()
