from pathlib import Path
import logging
from datetime import datetime

log_file_path = Path(__file__).parent / "hb_test.log"
log_file_path.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(filename=str(log_file_path), level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def time_to_seconds(time_str):
    try:
        time_obj = datetime.strptime(time_str, "%H:%M:%S")
        return time_obj
    except ValueError as e:
        logging.error(f"Error converting time: {time_str}. Error: {e}")
        return None

def analyze_log(filename:str = "hblog.txt"):
    filename = Path(__file__).parent / filename
    print(f"Reading from file: {filename}")

    try:
        with open(filename, mode="r") as f:
            lines = f.readlines()

        timestamps = []
        for line in lines:
            if "Timestamp" in line:
                time_str = line.split("Timestamp")[1].split()[0]
                seconds = time_to_seconds(time_str)
                if seconds is not None:
                    timestamps.append(seconds)

        unique_sorted_timestamps = sorted(set(timestamps))

        for i in range(1, len(unique_sorted_timestamps)):
            heartbeat = unique_sorted_timestamps[i] - unique_sorted_timestamps[i-1]

            if 31 < heartbeat <= 33:
                logging.warning(f"Heartbeat between {unique_sorted_timestamps[i-1]} and {unique_sorted_timestamps[i]} was {heartbeat} seconds")
            elif heartbeat > 33:
                logging.error(f"Heartbeat between {unique_sorted_timestamps[i-1]} and {unique_sorted_timestamps[i]} was {heartbeat} seconds")

    except FileNotFoundError:
        logging.error(f"File {filename} not found")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    analyze_log()
