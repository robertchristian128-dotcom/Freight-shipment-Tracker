from flask import Flask, render_template, request, redirect, url_for, flash, send_file
import gspread
from google.oauth2.service_account import Credentials
from datetime import date
import io
import os
import sys

app = Flask(__name__)
app.secret_key = "freight_tracker_secret_key"

# Import your existing modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

def get_sheet():
    from config import SPREADSHEET_ID, SCOPES
    creds = Credentials.from_service_account_file("credentials.json", scopes=SCOPES)
    client = gspread.authorize(creds)
    return client.open_by_key(SPREADSHEET_ID).sheet1

def get_all_shipments():
    sheet = get_sheet()
    return sheet.get_all_records()

# ─── ROUTES ───────────────────────────────────────────────
@app.route("/archived")
def archived_shipments():
    try:
        import sheets
        archive_sheet = sheets.get_archive_sheet()
        records = archive_sheet.get_all_records()
        return render_template("archived.html", shipments=records)
    except Exception as e:
        flash(f"Error loading archive: {str(e)}", "error")
        return redirect(url_for("index"))

@app.route("/")
def index():
    shipments = get_all_shipments()
    
    total = len(shipments)
    pending = len([s for s in shipments if s["Status"] == "Pending"])
    in_transit = len([s for s in shipments if s["Status"] == "In Transit"])
    arrived = len([s for s in shipments if s["Status"] == "Arrived at Port"])
    cleared = len([s for s in shipments if s["Status"] == "Cleared"])
    delivered = len([s for s in shipments if s["Status"] == "Delivered"])
    delayed = len([s for s in shipments if s["Status"] == "Delayed"])
    
    stats = {
        "total": total,
        "pending": pending,
        "in_transit": in_transit,
        "arrived": arrived,
        "cleared": cleared,
        "delivered": delivered,
        "delayed": delayed
    }
    
    return render_template("index.html", shipments=shipments, stats=stats)

@app.route("/add", methods=["GET", "POST"])
def add_shipment():
    if request.method == "POST":
        try:
            sheet = get_sheet()
            new_shipment = [
                request.form["shipment_id"],
                request.form["client_name"],
                request.form["client_email"],
                request.form["origin"],
                request.form["destination"],
                request.form["status"],
                request.form["eta"],
                str(date.today().strftime("%d/%m/%Y"))
            ]
            sheet.append_row(new_shipment)
            flash("Shipment added successfully!", "success")
            return redirect(url_for("index"))
        except Exception as e:
            flash(f"Error adding shipment: {str(e)}", "error")
    
    return render_template("add_shipment.html")

@app.route("/run-monitor")
def run_monitor():
    try:
        from monitor import check_shipments
        alerts = check_shipments()
        flash(f"Monitor ran successfully! {len(alerts)} client(s) notified.", "success")
    except Exception as e:
        flash(f"Monitor error: {str(e)}", "error")
    return redirect(url_for("index"))

@app.route("/send-report")
def send_report():
    try:
        from report import send_daily_report
        send_daily_report()
        flash("Daily report sent to manager successfully!", "success")
    except Exception as e:
        flash(f"Report error: {str(e)}", "error")
    return redirect(url_for("index"))

@app.route("/download-report")
def download_report():
    try:
        shipments = get_all_shipments()
        
        delivered = [s for s in shipments if s["Status"] == "Delivered"]
        delayed = [s for s in shipments if s["Status"] == "Delayed"]
        in_transit = [s for s in shipments if s["Status"] == "In Transit"]
        pending = [s for s in shipments if s["Status"] == "Pending"]
        cleared = [s for s in shipments if s["Status"] == "Cleared"]
        arrived = [s for s in shipments if s["Status"] == "Arrived at Port"]


        report = f"""DAILY SHIPMENT REPORT — {date.today()}
========================================
SUMMARY
========================================
Total Shipments:        {len(shipments)}
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

        report += "\n========================================\nIN TRANSIT:\n========================================\n"
        for s in in_transit:
            report += f"- {s['Shipment ID']} | {s['Client Name']} | {s['Origin']} to {s['Destination']} | ETA: {s['ETA']}\n"

        report += "\n========================================\nARRIVED AT PORT:\n========================================\n"
        for s in arrived:
            report += f"- {s['Shipment ID']} | {s['Client Name']} | {s['Origin']} to {s['Destination']} | ETA: {s['ETA']}\n"

        report += "\n========================================\nCLEARED:\n========================================\n"
        for s in cleared:
            report += f"- {s['Shipment ID']} | {s['Client Name']} | {s['Origin']} to {s['Destination']} | ETA: {s['ETA']}\n"

        report += "\n========================================\nDELAYED SHIPMENTS:\n========================================\n"
        for s in delayed:
            report += f"- {s['Shipment ID']} | {s['Client Name']} | {s['Origin']} to {s['Destination']} | ETA: {s['ETA']}\n"

        report += "\n========================================\nDELIVERED TODAY:\n========================================\n"
        for s in delivered:
            report += f"- {s['Shipment ID']} | {s['Client Name']} | {s['Origin']} to {s['Destination']}\n"

        buffer = io.BytesIO()
        buffer.write(report.encode('utf-8'))
        buffer.seek(0)

        return send_file(
            buffer,
            as_attachment=True,
            download_name=f"freight_report_{date.today()}.txt",
            mimetype='text/plain'
        )
    except Exception as e:
        flash(f"Download error: {str(e)}", "error")
        return redirect(url_for("index"))

@app.route("/archive/<shipment_id>")
def archive_shipment_route(shipment_id):
    try:
        import sheets
        success = sheets.archive_shipment(shipment_id)
        if success:
            flash(f"Shipment {shipment_id} archived successfully!", "success")
        else:
            flash(f"Shipment {shipment_id} not found.", "error")
    except Exception as e:
        flash(f"Archive error: {str(e)}", "error")
        print(f"ARCHIVE ERROR DETAIL: {str(e)}")
    return redirect(url_for("index"))
if __name__ == "__main__":
    app.run(debug=True)

    print(f"ARCHIVE ERROR DETAIL: {str(e)}")