# 🚀 Quantsapp Data Automation System

An intelligent automation system that fetches **Unusual Option Activity** data from [Quantsapp](https://web.quantsapp.com), exports it to Excel, and sends real-time summaries and visual reports to **Telegram** — all fully automated.

---

## 🧭 Overview

This project automates the process of collecting and analyzing options data for traders.  
It continuously scrapes filtered data (like Signal Type = IV, Opt Type = ALL, Built-up Type = ALL) from Quantsapp, logs it into Excel, and generates daily performance reports with charts.

The system eliminates manual copy-paste work and provides actionable insights every 30 minutes directly to your Telegram bot.

---

## ⚙️ Features

✅ **Automated Web Scraping** — Fetches live data using Selenium every 30 mins (configurable).  
✅ **Excel Data Logging** — Appends each dataset to `output/Quantsapp_Unusual_Activity.xlsx`.  
✅ **Daily Summary Sheet** — Automatically computes average, min, and max % changes per day.  
✅ **Smart Formatting** — Auto-adjusts column widths and highlights positive/negative % in color.  
✅ **Visual Report Generator (PDF)** — Creates daily performance charts.  
✅ **Telegram Integration** — Sends real-time updates and daily PDF reports.  
✅ **Retry & Error Handling** — Handles page load issues and Excel locks gracefully.  
✅ **Auto Scheduling** — Runs continuously, with safe shutdown via Ctrl+C.

---

## 🧩 Project Structure


PythonProject/
│
├── main.py # Main automation logic
├── config.json # Configuration (URL, intervals, etc.)
├── requirements.txt # Python dependencies
├── .env # Telegram credentials (not uploaded)
│
├── helpers/
│ ├── excel_utils.py # Excel append and write functions
│ ├── notify.py # Telegram bot message sender
│ ├── report_utils.py # Daily summary and formatting logic
│ └── report_visuals.py # Chart and PDF generation
│
├── output/ # Live Excel data
├── reports/ # Auto-generated PDF reports
└── logs/ # System logs


---

## ⚙️ Setup Guide

### **1️⃣ Clone the Repo**
```bash
git clone https://github.com/Harivignz/quantsapp-automation.git
cd quantsapp-automation

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Create .env

In the root folder, create a file named .env:

TELEGRAM_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here

4️⃣ Adjust Config

Edit config.json to set intervals and file paths:

{
  "start_url": "https://web.quantsapp.com/unusual-option-activity",
  "fetch_interval_minutes": 30,
  "output_file": "output/Quantsapp_Unusual_Activity.xlsx",
  "sheet_name": "Data_Log",
  "headless": false,
  "max_table_wait_seconds": 15,
  "auto_refresh_page": true
}

5️⃣ Run
python main.py


Login to Quantsapp manually (OTP once), apply filters, and press Enter.
The system handles everything else automatically.

📊 Telegram Notifications

You’ll receive:

✅ Data Fetch Status

⚠️ Error Alerts

📈 Daily Summary

📊 PDF Visual Reports

Example message:

📊 Quantsapp Daily Summary (2025-11-05)
• Total Entries: 340
• Avg Change %: 2.86
• Max Change %: +12.45
• Min Change %: -9.22
✅ Logged successfully in Excel.

💾 Reports & Output
Folder	Description
output/	Excel logs of every fetch
reports/	Daily PDF visual charts
logs/	Runtime logs and status reports
💡 Future Upgrades

🔁 Auto Backup System — Daily Excel copies

☁️ Google Sheets Sync — Live web dashboard

📊 Streamlit Web Dashboard — Interactive analytics

🤖 AI Alerts — Detect unusual trading patterns

🧑‍💻 Author

Hari Vignesh (@Harivignz)
AI & Data Science Enthusiast | Automation Developer

Then run these commands:

git add README.md
git commit -m "Added professional README.md"
git push
