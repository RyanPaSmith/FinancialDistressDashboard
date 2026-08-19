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


""" ================================================= 
    Financial Tags We Want to Pull From SEC Company Facts
    =================================================
"""
financial_tags = [
    "Assets",
    "AssetsCurrent",
    "Liabilities",
    "LiabilitiesCurrent",
    "StockholdersEquity",
    "NetIncomeLoss"
]