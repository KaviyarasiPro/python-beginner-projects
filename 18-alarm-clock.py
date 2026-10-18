from datetime import datetime, timedelta
import time

try:
    import winsound
except ImportError:
    winsound = None

print("=== ALARM CLOCK ===")

alarm_input = input("Set alarm time (HH:MM, 24-hour format): ")

try:
    alarm_time = datetime.strptime(alarm_input, "%H:%M").time()

    now = datetime.now()

    alarm_datetime = now.replace(
        hour=alarm_time.hour,
        minute=alarm_time.minute,
        second=0,
        microsecond=0
    )

    if alarm_datetime <= now:
        alarm_datetime += timedelta(days=1)

    print("Alarm set for:", alarm_datetime.strftime("%H:%M"))
    print("Waiting for alarm...")

    while datetime.now() < alarm_datetime:
        time.sleep(1)

    print("\n⏰ ALARM! Wake up!")

    for i in range(5):
        if winsound:
            winsound.Beep(1000, 1000)
        else:
            print("\a")
            time.sleep(1)

except ValueError:
    print("Invalid time! Enter the time in HH:MM format.")
    print("Example: 07:30")
