from src.services import all_company_financial_dataframes
from src.dictionary import financial_tags


from src.organize_financials import organize_company_financials_by_year
from src.financial_ratios import calculate_financial_ratios


def main():

    organized_company_financials = organize_company_financials_by_year()

    print(organized_company_financials)
    
    financial_ratios = calculate_financial_ratios(organized_company_financials)
    
    print(financial_ratios)


if __name__ == "__main__":
    main()
    
 