import time

print("=== STOPWATCH ===")

input("Press Enter to start the stopwatch...")
start_time = time.perf_counter()

input("Press Enter to stop the stopwatch...")
end_time = time.perf_counter()

elapsed_time = end_time - start_time

minutes = int(elapsed_time // 60)
seconds = elapsed_time % 60

print("\n=== STOPWATCH RESULT ===")
print(f"Elapsed Time: {minutes:02d}:{seconds:05.2f}")
print(f"Total Seconds: {elapsed_time:.2f}")
