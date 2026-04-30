import gspread
from google.oauth2.service_account import Credentials
from config import SPREADSHEET_ID, SCOPES

cope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
]

def get_sheet():
    creds = Credentials.from_service_account_file(
        r"C:\Users\HP\Desktop\Freight Tracker\credentials.json",
     scopes=scope
)
    client = gspread.authorize(creds)
    Sheets = client.open(FREIGHT-TRACKER).sheet1

def get_all_shipments():
    sheet = get_sheet()
    return sheet.get_all_records()

def update_last_seen(row_index, value):
    sheet = get_sheet()
    sheet.update_cell(row_index, 8, value)