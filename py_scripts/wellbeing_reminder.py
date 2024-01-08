import plyer
import schedule
import time

def send_notification(message):
    plyer.notification.notify(
        title='Reminder',
        message=message,
        timeout=10
    )

def drink_water_reminder():
    send_notification("Drink water plisssssss!")

def walk_reminder():
    send_notification("Uth jaa bhai kitne der se baitha hai")

def main():
    # Schedule reminders
    schedule.every(30).minutes.do(walk_reminder)
    schedule.every(2).hours.do(drink_water_reminder)

    # Run scheduled tasks
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
