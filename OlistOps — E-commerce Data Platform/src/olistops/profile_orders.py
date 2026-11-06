
import csv
from datetime import date
from pathlib import Path

root = Path(__file__).resolve().parents[2]

path = root / "data/raw/olist/olist_orders_dataset.csv"

statuses = {}
ids = set()

total = 0
duplicates = 0
delivered = 0
late = 0
on_time = 0
missing_dates = 0

with open(path, "r", encoding="utf-8-sig", newline="") as f:

    reader = csv.DictReader(f)

    for row in reader:
        total += 1

        order_id = row["order_id"]
        status = row["order_status"]

        if order_id in ids:
            duplicates += 1
        else:
            ids.add(order_id)

        if status not in statuses:
            statuses[status] = 0

        statuses[status] += 1

        if status == "delivered":
            delivered += 1

            actual = row["order_delivered_customer_date"]
            estimated = row["order_estimated_delivery_date"]

            if not actual or not estimated:
                missing_dates += 1
                continue

            actual_date = date.fromisoformat(actual[:10])
            estimated_date = date.fromisoformat(estimated[:10])

            if actual_date > estimated_date:
                late += 1
            else:
                on_time += 1

print("Total orders:", total)
print("Duplicate IDs:", duplicates)

for status in statuses:
    print(status, statuses[status])

print("Delivered:", delivered)
print("Late:", late)
print("On time:", on_time)
print("Missing delivery dates:", missing_dates)

valid = late + on_time

if valid > 0:
    percentage = late / valid * 100
    print("Late delivery rate:", round(percentage, 2))
