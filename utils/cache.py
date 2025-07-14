import json, time, os

def is_cache_valid(file, ttl):
    if not os.path.exists(file):
        return False
    return time.time() - os.path.getmtime(file) < ttl

def load_cache(file):
    with open(file, "r", encoding="utf-8") as f:
        return json.load(f)

def save_cache(file, data):
    os.makedirs(os.path.dirname(file), exist_ok=True)
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f)
