import argparse
import csv
import os

LABELS = ["Business", "Personal", "Advertising"]

INSTRUCTION = f"""
Thank you for participating in our annotation task!
Your job is to look at the data points (email content) and decide whether they are business-related, personal, or advertising.

Labels:
    (0) {LABELS[0]} - Business-related content
    (1) {LABELS[1]} - Personal content
    (2) {LABELS[2]} - Advertising content

To exit anytime, type 'exit'.
"""

DELIMITER = "=" * 50
KEY_COL = "file"
DATA_COL = "message"


def get_last_position(output_file):
    if os.path.exists(output_file):
        with open(output_file, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader, None)
            responses = list(reader)
        return len(responses)
    return 0


def read_data(input_file):
    data = []
    with open(input_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if DATA_COL not in reader.fieldnames:
            print(f"Error: Column '{DATA_COL}' not found in the CSV file.")
            return None
        for row in reader:
            data.append((row[KEY_COL].strip(), row[DATA_COL].strip()))
    return data


def main():
    parser = argparse.ArgumentParser(
        description="Annotate email messages with labels (Business, Personal, Advertising).")
    parser.add_argument(
        "filename", help="Path to the CSV file containing the emails.")

    args = parser.parse_args()

    input_file = args.filename
    output_file = f"{input_file.split('.')[0]}_output.csv"

    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        return

    data = read_data(input_file)
    if data is None:
        return

    last_position = get_last_position(output_file)

    print(INSTRUCTION)
    with open(output_file, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if last_position == 0:
            with open(output_file, "w", newline="", encoding="utf-8") as file:
                pass
            writer.writerow([KEY_COL, "label"])

        for key, message in data[last_position:]:
            print(
                f"\n{DELIMITER}\n\nData Instance:\n\n{'-' * 50}\n{message}\n{'-' * 50}")
            print("\nTo exit anytime, type 'exit'.\n")
            print(
                " ".join([f"({i}) {label}" for i, label in enumerate(LABELS)]))

            while True:
                label = input("Your label: ").strip()

                if label.lower() == "exit":
                    print("Progress saved. You can resume later.")
                    return

                if label.isdigit() and 0 <= int(label) < len(LABELS):
                    writer.writerow([key, LABELS[int(label)]])
                    break
                else:
                    print("Invalid input. Please enter 0, 1, or 2.")

    print("\nAll messages have been labeled. Thank you.\n")


if __name__ == "__main__":
    main()
