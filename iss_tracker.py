import requests
import os
import time


def log_action(module, action, status):
    timestamp = time.ctime()
    with open("logs.txt", "a", encoding="utf-8", errors="replace") as log:
        log.write(f"{timestamp} - [{module}] {action} - {status}\n")

def fetch_iss_location():
    url = "http://api.open-notify.org/iss-now.json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()  
        position = data["iss_position"]
        lat, lon = position["latitude"], position["longitude"]

        os.makedirs("data", exist_ok=True)
        with open("data/iss_data.txt", "a", encoding="utf-8", errors="replace") as f:
            f.write("\n ISS Real-Time Location:\n")
            f.write(f"Latitude: {lat}\nLongitude: {lon}\n")

        print(f"ISS is currently at Latitude: {lat}, Longitude: {lon}")
        log_action("ISS Tracker", "Fetched ISS location", "Success")
    except Exception as e:
        print(" Error fetching ISS location:", e)
        log_action("ISS Tracker", "Fetch failed", f"Failed - {e}")

if __name__ == "__main__":
    fetch_iss_location()
