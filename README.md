# news_scraper

This Python-based web scraper and notifier automates the extraction and delivery of news articles from a specified website directly to your Telegram chat. It seamlessly combines efficient web scraping techniques with Telegram Bot API integration, built for reliability, extensibility, and ease of maintenance. 🚀


Key Highlights:

🔍 Web Scraping with BeautifulSoup:

Utilizes precise CSS selectors to parse complex HTML structures and extract article URLs along with their published dates. Polite scraping is ensured by custom user-agent headers to minimize the risk of getting blocked.

📂 Idempotent Notification System:

Keeps track of previously sent URLs with a sent_links.json file, preventing duplicate notifications. This persistent state enables smooth incremental scraping across multiple runs.

🤖 Telegram API Integration:

Sends formatted article updates via the Telegram Bot API using HTML for rich text. Implements a retry mechanism with exponential backoff to guarantee message delivery even under unstable network conditions.

🔐 Secure Configuration Management:

Loads sensitive Telegram credentials (TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID) securely via environment variables with python-dotenv, avoiding hard-coded secrets and making deployments safer and more flexible.

📝 Robust Logging:

Logs all important actions, warnings, and errors with timestamps to scraper.log using UTF-8 encoding, providing comprehensive audit trails and simplifying debugging.

⚙️⏰ Automating the Scraper with crontab 📰🤖

You can schedule the scraper to run automatically at specific times using cron, which is a job scheduler available on most Unix-like systems including Ubuntu.
Example Workflow
    • Reset the sent links file daily at 7:00 AM (optional, if you want to clear the contents of the sent_links.json file).
    • Run the scraper every hour from 8:00 AM to 8:00 PM, and logging the output for troubleshooting and audit.

1. Shell Script to Run the Scraper
Create a shell script (e.g., run_scraper.sh) to activate your Python environment and run the scraper:
#!/bin/bash

# Navigate to your scraper project directory (replace with actual path)
cd /path/to/your/web_scraper

# Run the scraper using the Python version in your virtual environment
./.venv/bin/python3.13 app.py

Make sure to give the script execute permissions:
chmod +x /path/to/run_scraper.sh


2. Crontab Entries
Edit your user’s crontab with:
crontab -e


And add the following lines (replace paths accordingly):
text

# Reset sent_links.json daily at 7:00 AM (optional)
0 7 * * * > /full/path/to/sent_links.json

# Run scraper every hour between 8 AM and 8 PM, logging output and errors
0 8-20 * * * /full/path/to/run_scraper.sh >> /full/path/to/web_scraper_logfile.log 2>&1

