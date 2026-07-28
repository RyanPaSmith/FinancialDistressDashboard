from email import header
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
    ticker_dictionary.update({key :{ "cik" : str(match["cik_str"].iloc[0]).zfill(10), "title" : match["title"].iloc[0]}})

# print(ticker_dictionary)

financial_data_link = "https://data.sec.gov/api/xbrl/companyfacts/CIK" + str(ticker_dictionary.get("AAPL").get("cik")) +".json"
# print(financial_data_link)

financial_data_apple = requests.get(financial_data_link,headers=headers)
converted_financial_apple = json.loads(financial_data_apple.text)
df_apple = pd.DataFrame(converted_financial_apple)
print(df_apple)





    
        
    

















