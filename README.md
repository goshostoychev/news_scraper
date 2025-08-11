# 📰 news_scraper

A Python-based web scraper and notifier that extracts the latest news articles from a specified website and sends updates directly to your Telegram chat. Combining powerful web scraping with Telegram Bot API integration, this tool is designed for **reliability**, **extensibility**, and **ease of maintenance**. 🚀

***

## 📝 Features

- 🔍 **Web Scraping with BeautifulSoup**  
  Efficiently parses complex HTML using CSS selectors to fetch article URLs and publication dates. Uses custom user-agent headers to avoid bot detection.

- 📂 **Idempotent Notification System**  
  Tracks sent articles in a `sent_links.json` file to prevent duplicate notifications, enabling incremental scraping across multiple runs.

- 🤖 **Telegram API Integration**  
  Sends formatted messages via Telegram Bot API with HTML styling and supports retry on failure for reliable delivery.

- 🔐 **Secure Credentials Management**  
  Loads sensitive data such as `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` from environment variables using `python-dotenv`, avoiding hard-coded secrets.

- 📝 **Robust Logging**  
  Detailed logs with timestamps and UTF-8 encoding are saved to `scraper.log`, aiding debugging and operational auditing.

***

## ⚙️ Setup & Installation

1. **Clone this repository**:

git clone https://github.com/yourusername/news_scraper.git
cd news_scraper



2. **Create and activate a virtual environment**:

python3 -m venv .venv
source .venv/bin/activate



3. **Install dependencies**:

pip install -r requirements.txt



4. **Create a `.env` file** in the project root with your Telegram credentials:

TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here



***

## 🚀 Usage

Run the scraper manually by executing:

./.venv/bin/python3.13 app.py



Make sure your `.env` file is configured properly before running.

***

## ⚙️⏰ Automating the Scraper with Cron 📰🤖

You can automate the scraper to run periodically using `cron`.

### 1. Create a shell script `run_scraper.sh`:

#!/bin/bash
Navigate to your scraper directory (replace with your actual path)

cd /path/to/news_scraper
Run the scraper with your virtual environment’s Python

./.venv/bin/python3.13 app.py



Make the script executable:

chmod +x /path/to/run_scraper.sh



### 2. Setup crontab jobs:

Open crontab for editing:

crontab -e



Add these lines, replacing paths as needed:

Optional: Reset sent_links.json daily at 7AM to resend all articles

0 7 * * * > /full/path/to/sent_links.json
Run scraper hourly from 8AM to 8PM, logging output and errors

0 8-20 * * * /full/path/to/run_scraper.sh >> /full/path/to/web_scraper_logfile.log 2>&1



***

## 📌 Notes & Tips

- Using absolute paths in crontab avoids environment-related issues.
- Resetting `sent_links.json` is optional and causes the scraper to resend all articles daily.
- Log file redirection captures all output and errors for troubleshooting.
- Verify your cron jobs with:

systemctl status cron
grep CRON /var/log/syslog



***

## 🛠️ Troubleshooting & Support

- Check `scraper.log` for detailed logs.
- Make sure environment variables are correctly loaded via `.env`.
- Validate your Telegram bot token and chat ID.
- If you encounter scraping issues, verify if website structure has changed.
