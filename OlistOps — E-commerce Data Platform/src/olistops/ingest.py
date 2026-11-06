
import csv
from pathlib import Path

root = Path(__file__).resolve().parents[2]
data_path = root / "data" / "raw" / "olist"

files = sorted(data_path.glob("*.csv"))

for file in files:

    print("\nFile:", file.name)

    count = 0

    with open(file, "r", encoding="utf-8-sig", newline="") as f:

        reader = csv.DictReader(f)

        print("Columns:", reader.fieldnames)

        for row in reader:

            count += 1

            if count == 1:
                print("First row:", row)

    print("Total rows:", count)
