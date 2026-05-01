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

       # Alert for arrived at port
        if status == "Arrived at Port":
            subject = f"Shipment {shipment_id} Has Arrived at Port"
            body = f"""
Dear {client_name},

Your shipment {shipment_id} from {shipment['Origin']} 
has arrived at {shipment['Destination']}.

It is currently undergoing port processing and clearance.
We will notify you once it has been cleared.

Regards,
Freight Operations Team
            """
            send_email(client_email, subject, body)
            alerts.append(shipment)

        # Alert for In transit shipments
        if status == "In Transit":
            subject = f"Shipment {shipment_id} Is In Transit"
            body = f"""
Dear {client_name},

We want to inform you that your shipment {shipment_id} 
from {shipment['Origin']} to {shipment['Destination']}
is currently in transit and is proggressing as expected.

we will keep you updated on its delivery report

Regards,
Freight Operations Team
            """
            send_email(client_email, subject, body)
            alerts.append(shipment)

        
        # Alert for cleared shipments
        if status == "Cleared":
            subject = f"Shipment {shipment_id} Has Been Cleared"
            body = f"""
Dear {client_name},

Great news! Your shipment {shipment_id} has successfully 
cleared customs at {shipment['Destination']}.

It is now ready for final delivery.
We will notify you once it has been delivered.

Regards,
Freight Operations Team
            """
            send_email(client_email, subject, body)
            alerts.append(shipment)

    
        # Alert for pending shipments
        if status == "pending":
            subject = f"Shipment {shipment_id} Is Still pending"
            body = f"""
Dear {client_name},

 We want to inform you that your shipment{shipment_id} 
from {shipment['Origin']} to {shipment['Destination']}
is currently pending.

We are actively monitoring the status.
we will keep you informes.

Regards,
Freight Operations Team
            """
            send_email(client_email, subject, body)
            alerts.append(shipment)

        
    return alerts  