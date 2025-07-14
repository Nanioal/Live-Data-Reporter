# Live Data Reporter

**Live Data Reporter** is a Python-based terminal app that helps explore real-time information from space, finance, and global news — all from one interactive interface. It’s designed to spark curiosity in STEM topics by transforming raw APIs into readable, live insights.

---

## 🌍 Features

- 👨‍🚀 View astronauts currently in space (via Open Notify API)
- 🛰️ Track the real-time position of the International Space Station
- 📰 Fetch top 3 U.S. business headlines (via NewsAPI)
- 📈 Get IBM’s latest 5-minute open stock price (via Alpha Vantage)
- 📝 Save results to a file for later exploration
- 📜 All API interactions are logged with timestamps for transparency

---

## ⚙️ Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/live-data-reporter.git
   cd live-data-reporter
2. **Create and Activate Virtual** *Environment (optional but recommended)*

    ```bash
    python -m venv venv
    source venv/bin/activate  
3. **Install Requirements**

    ```bash
    pip install -r requirements.txt
4. **Configure API Keys**

    >Create a .env file in the root directory.

    >Copy the format from .env.example and insert your actual keys:

        NEWS_API_KEY=your_news_api_key_here
        STOCK_API_KEY=your_alpha_vantage_key_here

**🚀 How to Run**
    
    ```bash
    python main.py
    Then use the numbered menu to choose a feature: 1. View astronauts currently in space
                        2. Track ISS location
                        3. View news or stock
                        4. Exit
**📚 APIs Used**
    1. Open Notify

    2. NewsAPI

    3. Alpha Vantage
**📁 Folder Structure**
live-data-reporter/
├── data/
│   └── iss_data.txt          # Output file with astronauts + ISS location
├── images/
│   └── map.gif, iss.gif      # Optional turtle visualizations
├── .env.example              # Sample env format
├── main.py                   # Entry-point CLI
├── astronauts.py             # Astronaut data fetcher
├── iss_tracker.py            # ISS position tracker
├── news_or_stock.py          # Headlines and stock price tool
├── logs.txt                  # Timestamped action logs
├── README.md                 # You are here!
├── requirements.txt          # All dependencies
