from src.dictionary import headers, financial_tags
from src.parse_dictionary import ticker_dictionary
import requests
import json
import pandas as pd


""" ================================================= 
    Get All Companies Financial Info in Seperate Dictionaries
    =================================================
"""
all_company_financial_dataframes = {}

for key in ticker_dictionary:
    company_cik = ticker_dictionary.get(key).get("cik")
    company_financial_link = "https://data.sec.gov/api/xbrl/companyfacts/CIK" + company_cik + ".json"
    print(company_financial_link)

    company_financial_data = requests.get(company_financial_link, headers=headers)
    converted_financial_data = dict(json.loads(company_financial_data.text))

    company_financial_dataframes = {}

    for tag in financial_tags:
        try:
            financial_data = converted_financial_data.get("facts").get("us-gaap").get(tag).get("units").get("USD")

            financial_dataframe = pd.DataFrame(financial_data)
            financial_dataframe["ticker"] = key
            financial_dataframe["financial_tag"] = tag
            
            form = "10-K"
            fp = "FY"
            
            filter_financial_dataframe = financial_dataframe.loc[(financial_dataframe["form"] == form) & (financial_dataframe["fp"] == fp)] 
            
            company_financial_dataframes[tag] = filter_financial_dataframe

        except:
            print("Error, " + tag + " is not available for " + key)

    all_company_financial_dataframes[key] = company_financial_dataframes
    
    print("All data pulled - successful")
    
    print(all_company_financial_dataframes.get("AAPL").get("Assets"))