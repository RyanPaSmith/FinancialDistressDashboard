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
                
                
    # print(organized_company_financials.get("AAPL"))
    
    for key in organized_company_financials:
        for year in organized_company_financials[key]:
            year_assets = organized_company_financials[key][year]["Assets"]
            year_current_assets = organized_company_financials[key][year]["AssetsCurrent"]
            year_liabilities = organized_company_financials[key][year]["Liabilities"]
            year_current_liabilities = organized_company_financials[key][year]["LiabilitiesCurrent"]
            year_stockholders_equity = organized_company_financials[key][year]["StockholdersEquity"]
            net_income_loss = organized_company_financials[key][year]["NetIncomeLoss"]
            
            current_ratio = year_current_assets / year_current_liabilities
            
            print(key,year, "current ratio = " , current_ratio)
            
    
                
                
            
        
        # asset_dataframe = company_financial_dataframes.get("Assets")
        # current_asset_dataframe = company_financial_dataframes.get("AssetsCurrent")
        # liability_dataframe = company_financial_dataframes.get("Liabilities")
        # current_liabilities_dataframe = company_financial_dataframes.get("LiabilitiesCurrent")
        # stockholders_equity_dataframe = company_financial_dataframes.get("StockholdersEquity")
        # net_income_loss_dataframe = company_financial_dataframes.get("NetIncomeLoss")

        

if __name__ == "__main__":
    main()