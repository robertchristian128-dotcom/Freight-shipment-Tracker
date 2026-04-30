from monitor import check_shipments
from report import send_daily_report

if __name__ == "__main__":
    print("Running shipment monitor...")
    check_shipments()
    
    print("Sending daily report...")
    send_daily_report()
    
    print("Done.")