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
