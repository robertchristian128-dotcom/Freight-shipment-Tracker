from monitor import check_shipments
from report import send_daily_report

if __name__ == "__main__":
    print("Running shipment monitor...")
    check_shipments()
    
    print("Sending daily report...")
    send_daily_report()
    
    
try:
    send_email(message)
except Exception as e:
    with open("log.txt", "a") as f:
        f.write(f"Error: {e}\n")

with open("log.txt", "a") as f:
    f.write("Email sent successfully\n")        