import requests
import os
import json
import datetime as dt
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

STOCK = "NVDA"
COMPANY_NAME = "NVIDIA Corporation"
ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "stock_data.json")

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
alpha_endpoint = 'https://www.alphavantage.co/query'
alpha_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHAVANTAGE_API_KEY
}

if os.path.exists(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    print("Loaded data from stock_data.json")
else:
    r = requests.get(url=alpha_endpoint, params=alpha_params)
    r.raise_for_status()
    data = r.json()

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

    print("Saved API response to stock_data.json")


dates = list(data["Time Series (Daily)"])[:2]
yesterday_close = data["Time Series (Daily)"][dates[0]]["4. close"]
day_before_close = data["Time Series (Daily)"][dates[1]]["4. close"]

print(yesterday_close)
print(day_before_close)

diff = float(day_before_close) - float(yesterday_close)
percentage_change = abs(round((diff / float(day_before_close)) * 100))
print(diff, percentage_change)

if diff < 0:
    icon = "🔻"
else:
    icon = "🔺"

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
if percentage_change >= 5:
    news_endpoint = "https://newsapi.org/v2/everything"
    news_params = {
        "q": COMPANY_NAME,
        "from": yesterday_close,
        "to": yesterday_close,
        "language": "en",
        "sortBy": "popularity",
        "apiKey": NEWS_API_KEY,
        "pageSize": 3,
        "page": 1
    }
    response = requests.get(url=news_endpoint, params=news_params)
    response.raise_for_status()
    news_data = response.json()
#    print(news_data)

# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.
    account_sid = os.getenv('TWILIO_ACCT_SID')
    auth_token = os.getenv('AUTH_TOKEN')
    client = Client(account_sid, auth_token)
    
    for article in news_data["articles"]:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=f"{STOCK}: {icon}{percentage_change}%\nHeadline: {article['title']}\nBrief: {article['description']}\n",
            to='whatsapp:+17153489399'
        )
        print(message.status)


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
