from astronauts import fetch_astronauts
from iss_tracker import fetch_iss_location
from news_or_stock import fetch_news, fetch_stock

def menu():
    while True:
        print("\n🌍 Live Data Reporter Menu")
        print("1. View astronauts currently in space")
        print("2. Track the ISS location")
        print("3. View news or stock")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            fetch_astronauts()
        elif choice == "2":
            fetch_iss_location()
        elif choice == "3":
            sub = input("Press 1 for News or 2 for Stock: ")
            if sub == "1":
                fetch_news()
            elif sub == "2":
                fetch_stock()
            else:
                print("❌ Invalid sub-option.")
        elif choice == "4":
            print("👋 Exiting. Stay curious!")
            break
        else:
            print("❌ Invalid option. Please try again.")

if __name__ == "__main__":
    menu()
