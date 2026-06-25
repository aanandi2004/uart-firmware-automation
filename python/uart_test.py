#separate function for turning in the led, off led, button pressesd , button relsase, read command
#entered then only distance i measured basically indipendant commands 
'''from uart_controller import send_command, close_connection
import csv
from datetime import datetime


def main():

    print("Connected to Arduino\n")

    # ---------------- Sanity Tests ----------------
    print("--- Running Sanity Tests ---")
    print(f"VERSION Response: {send_command('VERSION')}")
    print(f"LED_ON Response: {send_command('LED ON')}")
    print(f"LED_OFF Response: {send_command('LED OFF')}")
    print("----------------------------\n")

    # ---------------- Test Cases ----------------
    test_cases = [
        {"name": "TC1", "cmd": "VERSION", "expected": "V1.3.0"},
        {"name": "TC2", "cmd": "LED ON", "expected": "LED IS ON"},
        {"name": "TC3", "cmd": "LED OFF", "expected": "LED IS OFF"},
        {"name": "TC4", "cmd": "STATUS", "expected": "BUTTON:"},
    ]

    results = []
    pass_count = 0
    fail_count = 0

    print("--- Starting Automation Framework ---")

    for iteration in range(3):
        print(f"\n--- Iteration {iteration + 1} ---")

        for case in test_cases:

            try:
                actual_response = send_command(case["cmd"])

                if case["expected"] in actual_response:
                    verdict = "TEST PASSED"
                    status = "PASS"
                    pass_count += 1
                else:
                    verdict = "TEST FAILED"
                    status = "FAIL"
                    fail_count += 1

                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                results.append({
                    "timestamp": timestamp,
                    "test_case": case["name"],
                    "command": case["cmd"],
                    "expected": case["expected"],
                    "actual": actual_response,
                    "result": status
                })

                print(
                    f"{case['name']} | Cmd: {case['cmd']} | "
                    f"Expected: '{case['expected']}' | "
                    f"Actual: '{actual_response}' -> {verdict}"
                )

            except Exception as e:
                print(f"ERROR executing {case['name']}: {e}")
                fail_count += 1

    # ---------------- Summary ----------------
    total = pass_count + fail_count
    pass_percentage = (pass_count / total) * 100 if total else 0

    print("\n==============================")
    print("        TEST SUMMARY")
    print("==============================")
    print(f"PASS: {pass_count}")
    print(f"FAIL: {fail_count}")
    print(f"TOTAL: {total}")
    print(f"PASS PERCENTAGE: {pass_percentage:.2f}%")
    print("==============================")

    # ---------------- CSV Report ----------------
    csv_filename = "uart_test_results.csv"

    with open(csv_filename, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "timestamp",
                "test_case",
                "command",
                "expected",
                "actual",
                "result",
            ],
        )

        writer.writeheader()
        writer.writerows(results)

    print(f"\nReport archived safely to: '{csv_filename}'")

    close_connection()
    print("Serial connection closed safely.")


if __name__ == "__main__":
    main()'''



#Button Pressed -> LED ON ->Start measuring distance ->Send distance over UART every 100 ms->Button Released
#->LED OFF ->Stop sending distance
