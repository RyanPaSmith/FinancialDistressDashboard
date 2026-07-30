from src.dictionary import headers, ticker_dictionary
import requests
import json

""" ================================================= 
    Convert Baseline Link to Apple Link Using Constructed Nested Dictionary
    =================================================
"""
financial_data_link = "https://data.sec.gov/api/xbrl/companyfacts/CIK" + str(ticker_dictionary.get("AAPL").get("cik")) +".json"
# print(financial_data_link)

""" ================================================= 
    Get Apples Financial Data In One Giant Nested Dictionary
    =================================================
"""
financial_data_apple = requests.get(financial_data_link,headers=headers)
converted_financial_apple = json.loads(financial_data_apple.text)
