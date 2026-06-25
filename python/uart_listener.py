from uart_controller import read_distance, close_connection
import csv
from datetime import datetime

SAFE_LIMIT = 30
WARNING_LIMIT = 100

safe_count = 0
warning_count = 0
out_count = 0
total = 0

min_distance = None
max_distance = None
sum_distance = 0

print("Listening...")

with open("live_log.csv", "w", newline="") as file:

    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Distance(cm)", "Status"])

    try:
        while True:

            data = read_distance()

            if data:

                distance = float(data.split()[1])

                if distance < SAFE_LIMIT:
                    status = "SAFE"
                    safe_count += 1

                elif distance < WARNING_LIMIT:
                    status = "WARNING"
                    warning_count += 1

                else:
                    status = "OUT OF RANGE"
                    out_count += 1

                total += 1
                sum_distance += distance

                if min_distance is None or distance < min_distance:
                    min_distance = distance

                if max_distance is None or distance > max_distance:
                    max_distance = distance

                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                writer.writerow([timestamp, distance, status])
                file.flush()

                print(f"{timestamp} | {distance:.2f} cm | {status}")

    except KeyboardInterrupt:
        print("\nStopped")

    finally:

        print("\n========== SUMMARY ==========")

        print(f"Total Samples : {total}")
        print(f"SAFE          : {safe_count}")
        print(f"WARNING       : {warning_count}")
        print(f"OUT OF RANGE  : {out_count}")

        if total > 0:
            print(f"Minimum       : {min_distance:.2f} cm")
            print(f"Maximum       : {max_distance:.2f} cm")
            print(f"Average       : {sum_distance/total:.2f} cm")

        print("=============================")

        close_connection()