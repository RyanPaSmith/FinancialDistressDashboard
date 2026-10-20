from src.services import all_company_financial_dataframes
from src.dictionary import financial_tags
from src.parse_dictionary import ticker_dictionary


from src.organize_financials import organize_company_financials_by_year
from src.financial_ratios import calculate_financial_ratios
from src.filing_services import build_company_filing_links
from src.filing_services import get_company_sec_filing
from src.filing_services import build_filing_document_links


def main():

    sec_filing_links = build_company_filing_links(ticker_dictionary)

    company_sec_filings = get_company_sec_filing(sec_filing_links)

    filing_document_links = build_filing_document_links(company_sec_filings, ticker_dictionary)

    for filing in filing_document_links:
        print(filing.get("ticker"), filing.get("form"), filing.get("link"))


if __name__ == "__main__":
    main()
    
 