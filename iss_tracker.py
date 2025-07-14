import requests
import os
import time
from utils.cache import is_cache_valid, load_cache, save_cache

ISS_URL = "http://api.open-notify.org/iss-now.json"
CACHE_FILE = "cache/iss.json"
CACHE_TTL = 300  # 5 minutes

def log_action(module, action, status):
    timestamp = time.ctime()
    with open("logs.txt", "a", encoding="utf-8", errors="replace") as log:
        log.write(f"{timestamp} - [{module}] {action} - {status}\n")

def show_iss_on_map(lat, lon):
    import turtle
    screen = turtle.Screen()
    screen.setup(width=720, height=360)
    screen.bgpic("images/map.png")
    screen.title("Real-Time ISS Position")

    screen.register_shape("images/iss.png")
    iss = turtle.Turtle()
    iss.shape("images/iss.png")
    iss.penup()

    # Convert lat/lon to screen coordinates
    x = (float(lon) + 180) * (720 / 360) - 360
    y = float(lat) * (360 / 180)
    iss.goto(x, y)
    turtle.done()

def fetch_iss_location():
    try:
        # ✅ Use cached data if recent
        if is_cache_valid(CACHE_FILE, CACHE_TTL):
            data = load_cache(CACHE_FILE)
        else:
            response = requests.get(ISS_URL)
            response.raise_for_status()
            data = response.json()
            save_cache(CACHE_FILE, data)

        position = data["iss_position"]
        lat, lon = position["latitude"], position["longitude"]

        os.makedirs("data", exist_ok=True)
        with open("data/iss_data.txt", "a", encoding="utf-8", errors="replace") as f:
            f.write("\n ISS Real-Time Location:\n")
            f.write(f"Latitude: {lat}\nLongitude: {lon}\n")

        print(f" ISS is currently at Latitude: {lat}, Longitude: {lon}")
        show_iss_on_map(lat, lon)
        log_action("ISS Tracker", "Fetched ISS location", "Success")

    except Exception as e:
        print(" Error fetching ISS location:", e)
        log_action("ISS Tracker", "Fetch failed", f"Failed - {e}")

if __name__ == "__main__":
    fetch_iss_location()
