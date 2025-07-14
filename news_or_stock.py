import requests
import os
import time
from dotenv import load_dotenv
from utils.cache import is_cache_valid, load_cache, save_cache

load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
STOCK_API_KEY = os.getenv("STOCK_API_KEY")

def log_action(module, action, status):
    timestamp = time.ctime()
    with open("logs.txt", "a", encoding="utf-8", errors="replace") as log:
        log.write(f"{timestamp} - [{module}] {action} - {status}\n")

def fetch_news():
    if not NEWS_API_KEY:
        print(" NEWS_API_KEY missing. Check your .env file.")
        log_action("News", "Missing API key", "Failed")
        return

    url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&pageSize=3&apiKey={NEWS_API_KEY}"
    cache_file = "cache/news.json"
    try:
        if is_cache_valid(cache_file, 300):
            data = load_cache(cache_file)
        else:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            save_cache(cache_file, data)

        articles = data.get("articles", [])
        print("\n Top Business Headlines:")
        for i, a in enumerate(articles, 1):
            print(f"\n{i}. {a['title']}\n{a['description']}\n{a['url']}")
        log_action("News", "Fetched headlines", "Success")
    except Exception as e:
        print(f" Error fetching news: {e}")
        log_action("News", "Fetch failed", f"Failed - {e}")

def fetch_stock():
    if not STOCK_API_KEY:
        print(" STOCK_API_KEY missing. Check your .env file.")
        log_action("Stock", "Missing API key", "Failed")
        return

    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={STOCK_API_KEY}"
    cache_file = "cache/stock.json"
    try:
        if is_cache_valid(cache_file, 300):
            data = load_cache(cache_file)
        else:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            save_cache(cache_file, data)

        if "Time Series (5min)" not in data:
            raise ValueError("Invalid or rate-limited stock response.")
        latest = list(data["Time Series (5min)"].values())[0]
        open_price = latest["1. open"]
        print(f"\n IBM Stock Open Price: ${open_price}")
        log_action("Stock", "Fetched IBM stock price", "Success")
    except Exception as e:
        print(f" Error fetching stock data: {e}")
        log_action("Stock", "Fetch failed", f"Failed - {e}")

if __name__ == "__main__":
    print("Choose:\n1. News\n2. Stock")
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        fetch_news()
    elif choice == "2":
        fetch_stock()
    else:
        print(" Invalid choice.")
