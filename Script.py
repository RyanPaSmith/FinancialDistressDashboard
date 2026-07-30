from email import header
from urllib.request import urlopen
from pandas import DataFrame, col
import requests
import json
import pandas as pd


SEC_TICKER_DICTIONARY = "https://www.sec.gov/files/company_tickers.json"

headers = {"User-Agent": "Ryan Smith FinancialDistressDashBoard ryanpasmith@gmail.com"}


""" ================================================= 
    Baseline Starting Nested Dictionary
    =================================================
"""
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

""" ================================================= 
    Get Dictionary From JSON & Convert to Pandas DF Then Loop Through Dictionary to Reconstruct Initial Empty Dictionary
    With Filled CIK'S and Titles Per Company
    =================================================
"""
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

""" ================================================= 
    Convert Baseline Link to Company Link Using Constructed Nested Dictionary
    =================================================
"""
# financial_links = {
#     "AAPL": {
#         "link": "",
#     },
#     "MSFT": {
#         "link": "",
#     },
#     "TSLA": {
#         "link": "",
#     }
# }

# for key in ticker_dictionary:
#     financial_links.update({key : {"link : " "https://data.sec.gov/api/xbrl/companyfacts/CIK" + str(ticker_dictionary.get(key).get("cik")) +".json"}})
# print(financial_links)

# """ ================================================= 
#     Get All Companies Financial Info in Seperate Dictionaries
#     =================================================
# """
# for key in financial_links:
#     financial_data_ + financial_links.get(key) = requests.get(financial_links.get("link"),headers=headers)

# # financial_data_all = requests.get(financial_links,headers=headers)
# # converted_financial_apple = json.loads(financial_data_apple.text)

# """ ================================================= 
#     Drill Down to Just Assets and Put in Pandas DataFrame
#     =================================================
# """
# # converted_financial_apple.get("facts").get("us-gaap").get("Assets").get("units").get("USD")
# # apple_assets_df = pd.DataFrame(converted_financial_apple)
# # # print(apple_assets_df.values)

for key in ticker_dictionary:
    company_cik = ticker_dictionary.get(key).get("cik")
    company_financial_link = "https://data.sec.gov/api/xbrl/companyfacts/CIK" + company_cik +".json"
    print(company_financial_link)
    company_financial_data = requests.get(company_financial_link,headers = headers)
    converted_financial_data = dict(json.loads(company_financial_data.text))
    try:
        assets = converted_financial_data.get("facts").get("us-gaap").get("Assets").get("units").get("USD")
        liabilities = converted_financial_data.get("facts").get("us-gaap").get("true").get("units").get("USD")
    except:
        print("Error, one of the tags is not available")
        break
    # converted_financial_data_dataframe = pd.DataFrame(assets)
    # converted_financial_data_dataframe = converted_financial_data_dataframe.drop(columns = ['entityName'])
    # print(converted_financial_data_dataframe)
    
    
    






    
        
    

















