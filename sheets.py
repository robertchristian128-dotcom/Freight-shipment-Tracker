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