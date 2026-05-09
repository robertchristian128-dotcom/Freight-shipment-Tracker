# 🚢 FreightTrack Pro — Freight Shipment Tracker & Automation System

A complete end-to-end freight shipment tracking and automation system built for freight forwarding agencies. The system eliminates manual client communication entirely by automating notifications, invoice generation, and reporting at every stage of a shipment's journey.

---

## 🎯 What This System Does

- **Live Shipment Tracking** — Connects to Google Sheets as a real-time shipment database
- **Automated Client Notifications** — Sends personalized emails when shipments are Delayed, Arrived at Port, Cleared or Delivered
- **Automated Invoice Generation** — Generates and emails professional PDF invoices in both USD and NGN when shipments are cleared
- **Daily Manager Reports** — Sends detailed summary reports to the agency manager every morning automatically
- **Professional Web Dashboard** — Full Flask dashboard for managing all shipments in one place
- **Shipment Archive** — Moves delivered shipments to archive for clean record keeping
- **Activity Logging** — Logs all system activity with timestamps
- **Task Scheduler** — Runs automatically every morning without manual intervention

---

## 🖥️ Dashboard Features

- View all active shipments with color coded status badges
- Add new shipments via clean web form
- Edit any shipment details and status directly from the dashboard
- Archive delivered shipments with one click
- Run the shipment monitor manually
- Email daily report to manager with one click
- Download daily report as text file
- View full archive of all delivered shipments

---

## 📊 Shipment Status Flow

```
Pending → In Transit → Arrived at Port → Cleared → Delivered → Archived
```

| Status | Client Notified | Invoice Generated |
|--------|----------------|------------------|
| Pending | ✗ | ✗ |
| In Transit | ✗ | ✗ |
| Arrived at Port | ✅ Email | ✗ |
| Cleared | ✅ Email + PDF Invoice | ✅ |
| Delayed | ✅ Email | ✗ |
| Delivered | ✅ Email | ✗ |

---

## 🛠️ Built With

- **Python 3** — Core programming language
- **Flask** — Web dashboard framework
- **Google Sheets API** — Live shipment database via gspread
- **Google Auth** — Service account authentication
- **SMTP (Gmail)** — Email automation
- **ReportLab** — Professional PDF invoice generation
- **Git & GitHub** — Version control
- **Windows Task Scheduler** — Automated daily execution

---

## 📁 Project Structure

```
Freight-Tracker/
├── app.py                  # Flask web dashboard & all routes
├── main.py                 # Entry point — runs monitor & report
├── sheets.py               # Google Sheets API connection & operations
├── monitor.py              # Shipment status checker & email triggers
├── emailer.py              # Email sending (plain text & HTML with attachment)
├── report.py               # Daily manager report generator
├── invoice_generator.py    # PDF & HTML invoice generation
├── csv_importer.py         # Bulk import CSV data to Google Sheet
├── sheet_writer.py         # Add single shipments via Python
├── config.py               # Credentials & settings (not on GitHub)
├── credentials.json        # Google service account key (not on GitHub)
├── requirements.txt        # Project dependencies
├── log.txt                 # System activity log
├── freight_mock_data.csv   # Mock shipment data for demos
├── .gitignore              # Files excluded from GitHub
├── README.md               # Project documentation
├── invoices/               # Generated PDF invoices (not on GitHub)
└── templates/
    ├── index.html          # Main dashboard
    ├── add_shipment.html   # Add new shipment form
    ├── edit_shipment.html  # Edit shipment form
    └── archived.html       # Archive page
```

---

## ⚙️ Setup Instructions

### 1 — Clone the repository
```bash
git clone https://github.com/yourusername/freight-tracker.git
cd freight-tracker
```

### 2 — Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3 — Install dependencies
```bash
pip install -r requirements.txt
```

### 4 — Set up Google Sheets API
- Go to [Google Cloud Console](https://console.cloud.google.com)
- Create a new project
- Enable **Google Sheets API** and **Google Drive API**
- Go to IAM & Admin → Service Accounts
- Create a service account and download the JSON key
- Rename it to `credentials.json` and place it in the project root
- Share your Google Sheet with the service account email as Editor

### 5 — Set up Gmail App Password
- Go to myaccount.google.com → Security → 2 Step Verification → App Passwords
- Generate a new app password
- Use this as your EMAIL_PASSWORD — not your regular Gmail password

### 6 — Configure config.py
```python
EMAIL_ADDRESS = "your@gmail.com"
EMAIL_PASSWORD = "your_gmail_app_password"
MANAGER_EMAIL = "manager@agency.com"
SPREADSHEET_ID = "your_spreadsheet_id"
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]
```

### 7 — Set up Google Sheet
Create a sheet with these exact column headers —

| Shipment ID | Client Name | Client Email | Origin | Destination | Status | ETA | Last Updated |

Create a second sheet tab named exactly **Archive**

### 8 — Update agency details in invoice_generator.py
```python
AGENCY_NAME = "Your Agency Name"
AGENCY_ADDRESS = "Your Address"
AGENCY_PHONE = "Your Phone"
AGENCY_EMAIL = "Your Email"
AGENCY_RC = "Your RC Number"
BANK_NAME = "Your Bank"
ACCOUNT_NAME = "Your Account Name"
ACCOUNT_NUMBER = "Your Account Number"
USD_TO_NGN = 1580  # Update exchange rate as needed
```

---

## 🚀 How to Run

### Run the automation system (monitor + report)
```bash
python main.py
```

### Run the web dashboard
```bash
python app.py
```
Then open your browser and go to `http://127.0.0.1:5000`

### Import CSV data to Google Sheet
```bash
python csv_importer.py
```

### Add a single shipment via Python
```bash
python sheet_writer.py
```

### Push changes to GitHub
```bash
git add .
git commit -m "Your commit message"
git push origin main
```

---

## 📧 Automated Email Triggers

When the monitor runs, it automatically sends emails based on shipment status —

**Client Emails:**
- Arrived at Port → Port arrival notification
- Cleared → Clearance notification + PDF invoice attached
- Delayed → Delay notification
- Delivered → Delivery confirmation

**Manager Emails:**
- Daily report covering all shipment statuses — sent every morning automatically

---

## 📄 Invoice Features

Automatically generated when a shipment is Cleared —

- Professional PDF invoice attached to email
- HTML invoice embedded in email body
- Itemized charges — Ocean Freight, Port Handling, Customs Clearing, Documentation, Terminal Gate Fee
- VAT calculated at 7.5%
- Dual currency — USD and NGN
- Payment instructions included
- Invoice saved to invoices/ folder

---

## 📦 Dependencies

```
gspread
google-auth
google-auth-oauthlib
google-auth-httplib2
flask
reportlab
```

Install all with —
```bash
pip install -r requirements.txt
```

---

## 🔒 Security

The following files are excluded from GitHub via .gitignore —

```
credentials.json    # Google service account private key
config.py           # Email credentials and Spreadsheet ID
invoices/           # Client invoice PDFs
freight_mock_data.csv
```

Never commit credentials to any repository.

---

## 🗺️ Roadmap

- [ ] Deploy to Railway or Render for 24/7 online access
- [ ] Login authentication for dashboard access control
- [ ] WhatsApp notifications via Twilio
- [ ] Search and filter shipments by status, date or client
- [ ] Analytics page — delivery rates, delay trends, performance metrics
- [ ] Multi-agency support
- [ ] SMS notifications
- [ ] Database migration from Google Sheets to PostgreSQL

---

## 👨🏾‍💻 Developer

Built by **Christian Arinze**
Freight & Logistics Automation Specialist
Lagos, Nigeria

[GitHub](https://github.com/yourusername) | [Upwork](https://upwork.com/yourprofile)

---

*Built with Python, Flask, Google Sheets API, and a lot of debugging 🚀*