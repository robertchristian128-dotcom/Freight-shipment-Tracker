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
    pending = [s for s in shipments if s["Status"] == "Pending"]
    cleared = [s for s in shipments if s["Status"] == "Cleared"]
    arrived = [s for s in shipments if s["Status"] == "Arrived at Port"]

    report = f"""
DAILY SHIPMENT REPORT — {date.today()}

========================================
SUMMARY
========================================
Total Shipments:        {total}
Pending:                {len(pending)}
In Transit:             {len(in_transit)}
Arrived at Port:        {len(arrived)}
Cleared:                {len(cleared)}
Delivered:              {len(delivered)}
Delayed:                {len(delayed)}

========================================
PENDING SHIPMENTS:
========================================
"""
    for s in pending:
        report += f"- {s['Shipment ID']} | {s['Client Name']} | {s['Origin']} to {s['Destination']} | ETA: {s['ETA']}\n"

    report += """
========================================
IN TRANSIT:
========================================
"""
    for s in in_transit:
        report += f"- {s['Shipment ID']} | {s['Client Name']} | {s['Origin']} to {s['Destination']} | ETA: {s['ETA']}\n"

    report += """
========================================
ARRIVED AT PORT:
========================================
"""
    for s in arrived:
        report += f"- {s['Shipment ID']} | {s['Client Name']} | {s['Origin']} to {s['Destination']} | ETA: {s['ETA']}\n"

    report += """
========================================
CLEARED:
========================================
"""
    for s in cleared:
        report += f"- {s['Shipment ID']} | {s['Client Name']} | {s['Origin']} to {s['Destination']} | ETA: {s['ETA']}\n"

    report += """
========================================
DELAYED SHIPMENTS:
========================================
"""
    for s in delayed:
        report += f"- {s['Shipment ID']} | {s['Client Name']} | {s['Origin']} to {s['Destination']} | ETA: {s['ETA']}\n"

    report += """
========================================
DELIVERED TODAY:
========================================
"""
    for s in delivered:
        report += f"- {s['Shipment ID']} | {s['Client Name']} | {s['Origin']} to {s['Destination']}\n"

    send_email(MANAGER_EMAIL, f"Daily Freight Report - {date.today()}", report)
    print("Manager report sent successfully")

