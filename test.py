import io
import sys
from bs4 import BeautifulSoup
import requests
import time

BOT_TOKEN = '6363247128:AAGb2pd2wpjv121_dSLH1o_zBIGEnIqtJ-E'
CHAT_ID = 304630156

def send_to_telegram(message):
    try:
       
        api_url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
        
      
        params = {
            'chat_id': CHAT_ID,
            'text': message,
            'parse_mode': 'HTML'  
        }

        
        response = requests.post(api_url, params=params)

      
        if response.status_code != 200:
            print(f"Failed to send message to Telegram. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending message to Telegram: {e}")

def scrape_and_send_to_telegram():
    url = 'https://www.ethiopia-insight.com/category/newsanalysis/'

   
    response = requests.get(url)

    
    if response.status_code == 200:
       
        soup = BeautifulSoup(response.content, 'html.parser')

       
        news_headers = soup.find_all('header', class_='entry-header')

       
        message = ""
        for header in news_headers:
            title_anchor = header.find('h2', class_='entry-title').find('a')
            if title_anchor:
                title_text = title_anchor.text.strip()
                title_link = title_anchor['href']
                message += f"<b>Title:</b> {title_text}\n<b>Link:</b> {title_link}\n\n"

       
        print("Sending message to Telegram...")
        send_to_telegram(message)

    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")


while True:
    scrape_and_send_to_telegram()
   
    time.sleep(30)
