import requests
from bs4 import BeautifulSoup
import time

BOT_TOKEN = '6363247128:AAGb2pd2wpjv121_dSLH1o_zBIGEnIqtJ-E'
CHAT_ID = 304630156

url = 'https://www.ethiopia-insight.com/category/newsanalysis/'

def send_to_telegram(message):
    try:
        api_url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
        params = {
            'chat_id': CHAT_ID,
            'text': message,
            'parse_mode': 'HTML'  
        }
        print("Sending message to Telegram...")
        response = requests.post(api_url, params=params)
        if response.status_code != 200:
            print(f"Failed to send message to Telegram. Status code: {response.status_code}")
        else:
            print("Message sent to Telegram successfully.")
    except Exception as e:
        print(f"Error sending message to Telegram: {e}")

def scrape_and_send():
    
    response = requests.get(url)

    
    if response.status_code == 200:
       
        soup = BeautifulSoup(response.content, 'html.parser')

    
        entries = soup.find_all('div', class_='meta-image')

        for entry in entries:
            
            link = entry.find('a')['href']

            
            entry_title = entry.find_next('h2', class_='entry-title')
            title_link = entry_title.find('a')['href']
            title_text = entry_title.text.strip()

            
            message = f"Link: {link}\nEntry Title: {title_text}\nTitle Link: {title_link}"

          
            send_to_telegram(message)

    else:
        print("Failed to retrieve the webpage.")


while True: 
    scrape_and_send()
    time.sleep(30)
