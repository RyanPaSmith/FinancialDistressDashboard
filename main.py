from src.services import all_company_financial_dataframes
from src.dictionary import financial_tags
from src.parse_dictionary import ticker_dictionary


from src.organize_financials import organize_company_financials_by_year
from src.financial_ratios import calculate_financial_ratios
from src.filing_services import build_company_filing_links
from src.filing_services import get_company_sec_filing


def main():

    # organized_company_financials = organize_company_financials_by_year()

    # print(organized_company_financials)
    
    # financial_ratios = calculate_financial_ratios(organized_company_financials)
    
    # print(financial_ratios)
    
    sec_filing_links = build_company_filing_links(ticker_dictionary)
    
    # print(sec_filing_links)
    
    company_sec_filings = get_company_sec_filing(sec_filing_links)
    
    recent_filings = company_sec_filings.get("AAPL").get("filings").get("recent")

    for index, form in enumerate(recent_filings.get("form")):
        
        if form == "10-K" or form == "10-Q":
            
            primary_document = recent_filings.get("primaryDocument")[index]
            print(form, primary_document)


if __name__ == "__main__":
    main()
    
 