from src.dictionary import ticker_dictionary, SEC_TICKER_DICTIONARY, headers
import requests
import json
import pandas as pd

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