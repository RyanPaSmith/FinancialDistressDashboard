from src.services import all_company_financial_dataframes
from src.dictionary import financial_tags


def main():
    organized_company_financials = {}
    
    for key in all_company_financial_dataframes:
        
        # print(key)
        
        organized_company_financials[key] = {}

        company_financial_dataframes = all_company_financial_dataframes.get(key)
        
        for tag in financial_tags:
            tag_dataframe = company_financial_dataframes.get(tag)
            
            for index, row in tag_dataframe.iterrows():
                fiscal_year = row.get("fy")
                value = row.get("val")
                
                if fiscal_year not in organized_company_financials[key]:
                    organized_company_financials[key][fiscal_year] = {}
                
                organized_company_financials[key][fiscal_year][tag] = value
                
                
    print(organized_company_financials.get("AAPL"))
                
                
            
        
        # asset_dataframe = company_financial_dataframes.get("Assets")
        # current_asset_dataframe = company_financial_dataframes.get("AssetsCurrent")
        # liability_dataframe = company_financial_dataframes.get("Liabilities")
        # current_liabilities_dataframe = company_financial_dataframes.get("LiabilitiesCurrent")
        # stockholders_equity_dataframe = company_financial_dataframes.get("StockholdersEquity")
        # net_income_loss_dataframe = company_financial_dataframes.get("NetIncomeLoss")

        

if __name__ == "__main__":
    main()