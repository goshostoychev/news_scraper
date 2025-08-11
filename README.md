# news_scraper

This Python-based web scraper and notifier automates the extraction and delivery of news articles from a specified website to a Telegram chat. It combines efficient web scraping techniques with Telegram Bot API integration, designed for reliability, extensibility, and ease of maintenance.

Key highlights:


**Web Scraping with BeautifulSoup**:

Utilizes precise CSS selectors to parse HTML and extract article URLs and published dates from complex nested page structures. Custom user-agent headers ensure polite scraping and reduce the chance of being blocked.

**Idempotent Notification System**:

Maintains a sent_links.json file to track and exclude previously sent URLs, preventing repeated notifications. This state persistence supports incremental scraping across multiple script runs.

**Telegram API Integration**:

Sends article updates via Telegram Bot API with message formatting in HTML. Implements a retry mechanism with exponential backoff to enhance message delivery reliability under intermittent network conditions.

**Secure Configuration Management**:

Sensitive credentials (TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID) are loaded securely via environment variables using python-dotenv, avoiding hard-coded secrets and facilitating deployment in different environments.

**Robust Logging**:

Logs actions, warnings, and errors with timestamps and UTF-8 encoding to scraper.log, enabling effective debugging and operational auditing.
