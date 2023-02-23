import schedule
from datetime import datetime

from src.datacalls.update.update_data import UpdateData


def write_to_log():
    with open("logs/database.log", "a") as f:
        f.write(f"Database updated at {datetime.now()}\n")


def scheduled_update():
    UpdateData.update_data()
    write_to_log()
    print("Database updated")


def main():
    schedule.every().day.at("00:00").do(scheduled_update)


if __name__ == '__main__':
    main()
