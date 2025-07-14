import tkinter as tk
from astronauts import fetch_astronauts
from iss_tracker import fetch_iss_location
from news_or_stock import fetch_news, fetch_stock

def run_astronauts():
    fetch_astronauts()
    status_label.config(text="✅ Astronauts updated")

def run_iss():
    fetch_iss_location()
    status_label.config(text="✅ ISS location updated")

def run_news():
    fetch_news()
    status_label.config(text="✅ News fetched")

def run_stock():
    fetch_stock()
    status_label.config(text="✅ Stock price fetched")

app = tk.Tk()
app.title("Live Data Reporter")
app.geometry("400x300")

tk.Label(app, text="🛰️ Live Data Reporter", font=("Arial", 16)).pack(pady=10)

tk.Button(app, text="View Astronauts", command=run_astronauts).pack(fill="x", padx=40, pady=5)
tk.Button(app, text="Track ISS", command=run_iss).pack(fill="x", padx=40, pady=5)
tk.Button(app, text="Get News", command=run_news).pack(fill="x", padx=40, pady=5)
tk.Button(app, text="Get Stock", command=run_stock).pack(fill="x", padx=40, pady=5)

status_label = tk.Label(app, text="", fg="green", font=("Arial", 10))
status_label.pack(pady=20)

app.mainloop()
