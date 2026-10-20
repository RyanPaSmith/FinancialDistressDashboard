# data.sec.gov/submissions/CIK##########.json
from src.dictionary import headers
import requests
import json

def build_company_filing_links (ticker_dictionary):
    
    sec_filing_dictionary = {}
    
    for key in ticker_dictionary:
        company_dictionary = {}
        company_cik = ticker_dictionary.get(key).get("cik")
        company_filing_link = "https://data.sec.gov/submissions/CIK" + company_cik + ".json"
        company_dictionary.update({"link" : company_filing_link})
        
        sec_filing_dictionary.update({key : company_dictionary })
        
    return sec_filing_dictionary


def get_company_sec_filing(sec_filing_dictionary):

    all_company_sec_filings = {}  

    for key in sec_filing_dictionary:

        company_sec_data = requests.get(sec_filing_dictionary.get(key).get("link"), headers=headers)
        converted_sec_data = dict(json.loads(company_sec_data.text))

        all_company_sec_filings.update({key: converted_sec_data})  

    return all_company_sec_filings
    
    
        
        
        
    
        
    