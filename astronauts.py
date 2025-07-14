import requests
import os
import time
from utils.cache import is_cache_valid, load_cache, save_cache

ASTROS_URL = "http://api.open-notify.org/astros.json"
CACHE_FILE = "cache/astros.json"
CACHE_TTL = 300  # seconds

def log_action(module, action, status):
    timestamp = time.ctime()
    with open("logs.txt", "a", encoding="utf-8", errors="replace") as log:
        log.write(f"{timestamp} - [{module}] {action} - {status}\n")

def fetch_astronauts():
    try:
        # Use cached data if available
        if is_cache_valid(CACHE_FILE, CACHE_TTL):
            data = load_cache(CACHE_FILE)
        else:
            response = requests.get(ASTROS_URL)
            response.raise_for_status()
            data = response.json()
            save_cache(CACHE_FILE, data)

        astronauts = data.get("people", [])
        
        # Save to file
        os.makedirs("data", exist_ok=True)
        with open("data/iss_data.txt", "w", encoding="utf-8", errors="replace") as f:
            f.write(" Astronauts Currently in Space:\n")
            for person in astronauts:
                f.write(f"- {person['name']} aboard {person['craft']}\n")

        print(" Astronaut list saved to iss_data.txt")
        log_action("Astronauts", "Fetched astronaut list", "Success")

    except Exception as e:
        print(f" Error fetching astronaut data: {e}")
        log_action("Astronauts", "Fetch failed", f"Failed - {e}")

if __name__ == "__main__":
    fetch_astronauts()
