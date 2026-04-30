from sheets import get_all_shipments
from emailer import send_email
from config import MANAGER_EMAIL
from datetime import date

def send_daily_report():
    shipments = get_all_shipments()
    
    total = len(shipments)
    delivered = [s for s in shipments if s["Status"] == "Delivered"]
    delayed = [s for s in shipments if s["Status"] == "Delayed"]
    in_transit = [s for s in shipments if s["Status"] == "In Transit"]

    report = f"""
DAILY SHIPMENT REPORT — {date.today()}

Total Shipments: {total}
In Transit: {len(in_transit)}
Delivered Today: {len(delivered)}
Delayed: {len(delayed)}

DELAYED SHIPMENTS:
"""
    for s in delayed:
        report += f"- {s['Shipment ID']} | {s['Client Name']} | {s['Origin']} to {s['Destination']}\n"

    send_email(MANAGER_EMAIL, f"Daily Freight Report - {date.today()}", report)