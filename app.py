#!/usr/bin/python3

import json
import logging
import os
import requests
import time
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Script logging config
logging.basicConfig(
    filename='scraper.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S',
    encoding='utf-8'
)


# Get Telegram credentials from environment variables
def get_credentials():
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')

    if token and chat_id:
        return token, chat_id

    return None, None


# Load previously sent URLs from a json file
def load_sent_links():
    if os.path.exists('sent_links.json'):
        try:
            with open('sent_links.json', 'r', encoding='utf-8') as f:
                return set(json.load(f))
        except (json.JSONDecodeError, FileNotFoundError):
            logging.warning("Problem with sent_links.json file, starting fresh.")
            return set()
    return set()


# Save updated sent URLs to the json file
def save_sent_links(sent_links):
    try:
        with open('sent_links.json', 'w', encoding='utf-8') as f:
            json.dump(list(sent_links), f, ensure_ascii=False, indent=2)
    except Exception as e:
        logging.error(f"Could not save sent links: {e}")


# Send message to Telegram with simple retry
def send_telegram_message(text, token, chat_id):
    telegram_url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text,
        'parse_mode': 'HTML'
    }

    # Try 3 times if it fails
    for attempt in range(3):
        try:
            response = requests.post(telegram_url, data=payload, timeout=10)
            response.raise_for_status()
            logging.info("Message sent successfully")
            return True
        except requests.exceptions.RequestException as e:
            logging.warning(f"Attempt {attempt + 1} failed: {e}")
            if attempt < 2:  # Wait before retrying (but not on last attempt)
                time.sleep(2)

    logging.error("Failed to send message after 3 attempts")
    return False


# Fetch and parse articles from the website
def fetch_articles(url):
    try:
        # Add a user agent to avoid being blocked
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get(url, timeout=10, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        article_links = soup.select(
            'div.submain-articles.after-top-article > ul > li > div.article-title > h2 > a'
        )
        article_dates = soup.select(
            'div.submain-articles.after-top-article > ul > li > div.article-title '
            '> div.article-meta > span.article-date'
        )

        results = []
        for link_tag, date_tag in zip(article_links, article_dates):
            link = link_tag.get('href')
            date = date_tag.get_text(strip=True)

            if link and date:
                results.append({
                    'link': link,
                    'date': date
                })
        return results

    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching articles: {e}")
        return []


def main():
    logging.info("Script started")

    # Get the Telegram credentials
    telegram_token, telegram_chat_id = get_credentials()

    if not telegram_token or not telegram_chat_id:
        logging.error("Missing TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID environment variables")
        return

    url = 'https://www.dnes.bg/'

    # Load previously sent articles
    sent_links = load_sent_links()

    # Get new articles
    articles = fetch_articles(url)

    if not articles:
        logging.info('No articles found')
        return

    # Process each article
    new_articles_sent = 0
    for article in articles:
        link = article['link']
        date = article['date']

        if link not in sent_links:
            message = f"<b>{date}</b>\n{link}"

            if send_telegram_message(message, telegram_token, telegram_chat_id):
                sent_links.add(link)
                save_sent_links(sent_links)
                new_articles_sent += 1

                time.sleep(1)
            else:
                logging.error(f"Failed to send article: {link}")
                break
        else:
            logging.info(f"Already sent: {link}")
    logging.info(f"Script completed - sent {new_articles_sent} new article{'s' if new_articles_sent > 1 else ''}")


if __name__ == "__main__":
    main()
