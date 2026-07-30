import requests
from src.services import financial_data_link
from src.dictionary import headers
import json
import pandas as pd


def main():
    """ ================================================= 
        Get Apples Financial Data In One Giant Nested Dictionary
        =================================================
    """
    financial_data_apple = requests.get(financial_data_link,headers=headers)
    converted_financial_apple = json.loads(financial_data_apple.text)

    """ ================================================= 
        Drill Down to Just Apples Assets and Put in Pandas DataFrame
        =================================================
    """
    converted_financial_apple.get("facts").get("us-gaap").get("Assets").get("units").get("USD")
    apple_assets_df = pd.DataFrame(converted_financial_apple)
    print(apple_assets_df)


if __name__ == '__main__':
    main()