from datetime import datetime
import time

print("=== DIGITAL CLOCK ===")
print("Press Ctrl+C to stop the clock.\n")

try:
    while True:
        current_time = datetime.now().strftime("%I:%M:%S %p")

        print(f"\rCurrent Time: {current_time}", end="", flush=True)

        time.sleep(1)

except KeyboardInterrupt:
    print("\n\nDigital clock stopped.")
