import requests
import os
import json
import datetime as dt
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

STOCK = "PYPL"
COMPANY_NAME = "PayPal Holdings, Inc."
ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

file_path = "stock_data.json"

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

    with open("stock_data.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Saved API response to stock_data.json")


dates = list(data["Time Series (Daily)"])[:2]
yesterday_close = data["Time Series (Daily)"][dates[0]]["4. close"]
day_before_close = data["Time Series (Daily)"][dates[1]]["4. close"]

print(yesterday_close)
print(day_before_close)

diff = day_before_close - yesterday_close
percentage_change = abs(round((diff / float(day_before_close)) * 100))
print(percentage_change)

if percentage_change > 5:
    print("Get News")


# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
news_endpoint = "https://newsapi.org/v2/everything"
news_params = {
    "q": COMPANY_NAME,
    "from": day_before_close,
    "to": yesterday_close,
    "apiKey": NEWS_API_KEY
}
response = requests.get(url=news_endpoint, params=news_params)
response.raise_for_status()
news_data = response.json()
print(news_data)
# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.


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
