import gspread
from google.oauth2.service_account import Credentials
from config import SPREADSHEET_ID, SCOPES

def get_sheet():
    creds = Credentials.from_service_account_file(
        "credentials.json", scopes=SCOPES
    )
    client = gspread.authorize(creds)
    return client.open_by_key(SPREADSHEET_ID).sheet1

def get_all_shipments():
    sheet = get_sheet()
    return sheet.get_all_records()

def update_last_seen(row_index, value):
    sheet = get_sheet()
    sheet.update_cell(row_index, 8, value)

def get_archive_sheet():
    creds = Credentials.from_service_account_file(
        "credentials.json", scopes=SCOPES
    )
    client = gspread.authorize(creds)
    return client.open_by_key(SPREADSHEET_ID).worksheet("Archive")

def archive_shipment(shipment_id):
    import time
    
    for attempt in range(3):
        try:
            print(f"Attempt {attempt + 1}: Connecting to sheet...")
            sheet = get_sheet()
            print("Main sheet connected")
            
            print("Connecting to archive sheet...")
            archive_sheet = get_archive_sheet()
            print("Archive sheet connected")
            
            print("Fetching records...")
            records = sheet.get_all_records()
            all_values = sheet.get_all_values()
            print(f"Found {len(records)} records")
            
            for i, record in enumerate(records):
                if record["Shipment ID"] == shipment_id:
                    print(f"Found shipment at row {i + 2}")
                    row_index = i + 2
                    row_data = all_values[i + 1]
                    print(f"Row data: {row_data}")
                    archive_sheet.append_row(row_data)
                    print("Added to archive")
                    sheet.delete_rows(row_index)
                    print("Deleted from main sheet")
                    return True
                    
            print(f"Shipment {shipment_id} not found in records")
            return False
            
        except Exception as e:
            print(f"EXACT ERROR TYPE: {type(e).__name__}")
            print(f"EXACT ERROR MESSAGE: {str(e)}")
            if attempt < 2:
                time.sleep(3)
            else:
                raise Exception(f"Archive failed after 3 attempts: {str(e)}")