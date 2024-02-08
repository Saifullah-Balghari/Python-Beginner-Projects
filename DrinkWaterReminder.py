from plyer import notification
import winsound
import time


def send_notification():
    notification.notify(
        title='Drink Water Reminder',
        message='Please drink some water to stay hydrated!',
        timeout=5,
    )


print("After how many minutes you want a riminder\n (0 - 120)")
minutes = float(input("==> "))

if 0 <= minutes <= 120:
    seconds = minutes * 60
    time.sleep(seconds)
    winsound.Beep(1000, 500)
    send_notification()
else:
    print("please enter a value between 1 and 120 minutes")
