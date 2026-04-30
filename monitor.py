from datetime import datetime, date
from sheets import get_all_shipments
from emailer import send_email

def check_shipments():
    shipments = get_all_shipments()
    alerts = []

    for i, shipment in enumerate(shipments):
        status = shipment["Status"]
        eta = shipment["ETA"]
        client_email = shipment["Client Email"]
        client_name = shipment["Client Name"]
        shipment_id = shipment["Shipment ID"]

        # Alert for delayed shipments
        if status == "Delayed":
            subject = f"Shipment {shipment_id} Update"
            body = f"""
Dear {client_name},

We want to inform you that your shipment {shipment_id} 
from {shipment['Origin']} to {shipment['Destination']} 
is currently delayed.

Our team is working to resolve this. 
We will keep you updated.

Regards,
Freight Operations Team
            """
            send_email(client_email, subject, body)
            alerts.append(shipment)

        # Alert for delivered shipments
        if status == "Delivered":
            subject = f"Shipment {shipment_id} Delivered!"
            body = f"""
Dear {client_name},

Great news! Your shipment {shipment_id} has been 
successfully delivered to {shipment['Destination']}.

Thank you for choosing us.

Regards,
Freight Operations Team
            """
            send_email(client_email, subject, body)
            alerts.append(shipment)

    return alerts