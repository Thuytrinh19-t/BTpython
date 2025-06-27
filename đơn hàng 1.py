import json
from collections import defaultdict

data = [
    {
        "id": 0,
        "customer": "Minh",
        "items": [
            {"name": "Mouse", "quantity": 1, "unit_price": 25},
            {"name": "Watch", "quantity": 1, "unit_price": 600}
        ],
        "date": "2024-12-15"
    },
    {
        "id": 1,
        "customer": "Nam",
        "items": [
            {"name": "Laptop", "quantity": 1, "unit_price": 1200},
            {"name": "Mouse", "quantity": 2, "unit_price": 20}
        ],
        "date": "2024-12-01"
    }
]

sums_by_date = defaultdict(int)
for order in data:
    total = sum(item['quantity'] * item['unit_price'] for item in order['items'])
    sums_by_date[order['date']] += total


sorted_dates = sorted(sums_by_date.items())


for date, total in sorted_dates:
    print(f"{date} {total}")
