from urllib.request import urlopen
from pandas import DataFrame
import requests
import json
import pandas as pd


SEC_TICKER_DICTIONARY = "https://www.sec.gov/files/company_tickers.json"

headers = {"User-Agent": "Ryan Smith FinancialDistressDashBoard ryanpasmith@gmail.com"}

ticker_dictionary = {
    "AAPL": {
        "cik": "",
        "title": ""
    },
    "MSFT": {
        "cik": "",
        "title": ""
    },
    "TSLA": {
        "cik": "",
        "title": ""
    }
}

# print(ticker_dictionary)

data = requests.get(SEC_TICKER_DICTIONARY,headers=headers)
converted = json.loads(data.text)

df = pd.DataFrame(converted)
df = df.transpose()
# print(df)

" cik_str ticker title - to know what we're looking to match on and pull"
for key in ticker_dictionary:
    match = df[df["ticker"] == key]
    ticker_dictionary.update({key :{ "cik" :match["cik_str"].iloc[0], "title" :match["title"].iloc[0]}})

print(ticker_dictionary)

    
        
    

















