from email import header
from operator import ne
from urllib.request import urlopen
from numpy import mean
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
        current_assets = converted_financial_data.get("facts").get("us-gaap").get("AssetsCurrent").get("units").get("USD")
        liabilities = converted_financial_data.get("facts").get("us-gaap").get("Liabilities").get("units").get("USD")
        current_liabilties = converted_financial_data.get("facts").get("us-gaap").get("LiabilitiesCurrent").get("units").get("USD")
        stockholders_equity  = converted_financial_data.get("facts").get("us-gaap").get("StockholdersEquity").get("units").get("USD")
        net_income_loss = converted_financial_data.get("facts").get("us-gaap").get("NetIncomeLoss").get("units").get("USD")
        print("All data pulled - successful")
    except:
        print("Error, one of the tags is not available")
        break

    asset_dataframe = pd.DataFrame(assets)
    current_asset_dataframe = pd.DataFrame(current_assets)
    liability_dataframe = pd.DataFrame(liabilities)
    current_liabilities_Dataframe = pd.DataFrame(current_liabilties)
    stockholders_equity_dataframe = pd.DataFrame(stockholders_equity)
    net_income_loss_dataframe = pd.DataFrame(net_income_loss)
    
    """
    ================================================= 
    Current Ratio Calculation 
    =================================================
    """
    # Returns about 15 billion in for current_ratio of Apple, 70 Billion for Microsoft and 7 million for Tesla
    # This is just the mean value and should be done by row values per year  
    print(current_asset_dataframe['val'].mean() - current_liabilities_Dataframe['val'].mean())
    
    
    
    """
    ================================================= 
    Debt-Equity Ratio 
    =================================================
    """
    
    # Returns 259.36 billion for Apple, 268.55 billion for Microsoft, 40.17 billion for Tesla 
    # This is just the mean value and should be done by row values per year  
    print(liability_dataframe['val'].mean() + stockholders_equity_dataframe['val'].mean())
    

    
    
    
    
    
    






    
        
    

















