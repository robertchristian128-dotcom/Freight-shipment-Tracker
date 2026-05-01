# 🚢 Freight Shipment Tracker & Automated Alert System

A Python-based automation system built for freight forwarding 
agencies to track shipments and automatically notify clients 
at every stage of their shipment journey.

---

## 📌 What This System Does

- Connects to a live Google Sheet as a shipment database
- Monitors shipment statuses automatically
- Sends personalized email alerts to clients when:
  - Shipment arrives at port
  - Shipment clears customs
  - Shipment is delayed
  - Shipment is delivered
- Generates and emails a detailed daily summary 
  report to the agency manager
- Runs automatically every morning via task scheduler

---

## 🛠️ Built With

- Python 3
- Google Sheets API (gspread)
- Google Auth (Service Account)
- SMTP Email Automation (Gmail)
- Git & GitHub

---

## 📁 Project Structure
freight_tracker/
├── main.py          # Entry point - runs the full system
├── sheets.py        # Google Sheets API connection & data retrieval
├── monitor.py       # Shipment status checker & client email triggers
├── emailer.py       # Email sending via SMTP
├── report.py        # Daily manager report generator
├── config.py        # Configuration & credentials (not pushed to GitHub)
├── requirements.txt # Project dependencies
└── README.md        # Project documentation

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
- Go to Google Cloud Console
- Create a new project
- Enable Google Sheets API and Google Drive API
- Create a Service Account and download credentials.json
- Place credentials.json in the project root folder
- Share your Google Sheet with the service account email

### 5 — Configure config.py
```python
EMAIL_ADDRESS = "your@gmail.com"
EMAIL_PASSWORD = "your_gmail_app_password"
MANAGER_EMAIL = "manager@agency.com"
SPREADSHEET_ID = "your_google_spreadsheet_id"
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]
```

### 6 — Run the system
```bash
python main.py
```

---

## 📊 Google Sheet Structure

| Shipment ID | Client Name | Client Email | Origin | 
Destination | Status | ETA | Last Updated |

**Accepted Status Values:**
- Pending
- In Transit
- Arrived at Port
- Cleared
- Delivered
- Delayed

---

## 📧 Automated Email Triggers

| Status | Who Gets Notified |
|--------|------------------|
| Arrived at Port | Client |
| Cleared | Client |
| Delayed | Client |
| Delivered | Client |
| All statuses | Manager (daily report) |

---

## 🔒 Security Note

credentials.json and config.py are excluded from this 
repository via .gitignore to protect sensitive credentials.
Contact the developer to obtain setup assistance.

---

## 👨🏾‍💻 Developer

Built by Uzuegbunam Christian Arinze
Freight & Logistics Automation Specialist
Email:robertchristian128@gmail.com
Linkedin:Coming soon.....

---

## 🚀 Future Improvements

- Web dashboard for real time shipment visibility
- WhatsApp notification integration
- Automated invoice generation
- Multi-agency support