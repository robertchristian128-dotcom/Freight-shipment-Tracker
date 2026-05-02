import logging
from sheets import get_sheet

logging.basicConfig(
    filename='log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

def write_shipment_to_sheet(shipment):
    try:
        sheet = get_sheet()
        
        row = [
            shipment["Shipment ID"],
            shipment["Client Name"],
            shipment["Client Email"],
            shipment["Origin"],
            shipment["Destination"],
            shipment["Status"],
            shipment["ETA"],
            shipment["Last Updated"]
        ]
        
        sheet.append_row(row)
        logging.info(f"New shipment added: {shipment['Shipment ID']} - {shipment['Client Name']}")
        print(f"Shipment {shipment['Shipment ID']} added successfully")
        
    except Exception as e:
        logging.error(f"Failed to write shipment: {str(e)}")
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    new_shipment = {
        "Shipment ID": "FRT-2024-011",
        "Client Name": "Delta Offshore Supplies",
        "Client Email": "robertchristian128@gmail.com",
        "Origin": "Houston, USA",
        "Destination": "Onne Port, Rivers",
        "Status": "Pending",
        "ETA": "20/05/2026",
        "Last Updated": "02/05/2026"
    }
    
    write_shipment_to_sheet(new_shipment)