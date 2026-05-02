import csv
import logging
from sheets import get_sheet

logging.basicConfig(
    filename='log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

def import_csv_to_sheet(csv_filepath):
    try:
        sheet = get_sheet()
        
        with open(csv_filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
        
        sheet.clear()
        logging.info("Sheet cleared successfully")
        
        sheet.update(rows)
        logging.info(f"Successfully imported {len(rows) - 1} shipments to Google Sheet")
        print(f"Import complete - {len(rows) - 1} shipments loaded")
        
    except Exception as e:
        logging.error(f"CSV import failed: {str(e)}")
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    import_csv_to_sheet("freight_mock_data.csv")