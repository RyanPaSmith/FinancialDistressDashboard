# data.sec.gov/submissions/CIK##########.json
from matplotlib import ticker

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


def build_filing_document_links(company_sec_filings, ticker_dictionary):

    recent_filings = company_sec_filings.get("AAPL").get("filings").get("recent")

    company_cik = ticker_dictionary.get("AAPL").get("cik")
    company_cik = str(int(company_cik))

    filing_document_links = []
    
    for key in company_sec_filings:

        recent_filings = company_sec_filings.get(key).get("filings").get("recent")

        company_cik = ticker_dictionary.get(key).get("cik")
        company_cik = str(int(company_cik))
    
        for index, form in enumerate(recent_filings.get("form")):

            if form == "10-K" or form == "10-Q":
                primary_document = recent_filings.get("primaryDocument")[index]
                accession_number = recent_filings.get("accessionNumber")[index]
                accession_number = accession_number.replace("-", "")

                filing_link = "https://www.sec.gov/Archives/edgar/data/" + company_cik + "/" + accession_number + "/" + primary_document

                filing_document_links.append({"ticker" : key, "form": form,"link": filing_link})
    
    return filing_document_links
    
    
        
        
        
    
        
    