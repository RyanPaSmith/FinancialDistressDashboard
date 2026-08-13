from src.services import all_company_financial_dataframes
from src.dictionary import financial_tags


def main():
    organized_company_financials = {}
    
    for key in all_company_financial_dataframes:

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
    
    for key in organized_company_financials:
        for year in organized_company_financials[key]:
            
            if "AssetsCurrent" in organized_company_financials.get(key).get(year).keys() and "LiabilitiesCurrent" in organized_company_financials.get(key).get(year).keys():
                year_current_assets = organized_company_financials[key][year]["AssetsCurrent"]
                year_current_liabilities = organized_company_financials[key][year]["LiabilitiesCurrent"]
    
                current_ratio = year_current_assets / year_current_liabilities
                
                print(key,year, "current ratio = " , current_ratio)
                
            if "Liabilities" in organized_company_financials.get(key).get(year).keys() and "Assets" in organized_company_financials.get(key).get(year).keys():
                            year_assets = organized_company_financials[key][year]["Assets"]
                            year_liabilities = organized_company_financials[key][year]["Liabilities"]
                
                            debt_to_assets_ratio = year_liabilities / year_assets
                            
                            print(key,year, "debt to asset ratio = " , debt_to_assets_ratio)
                            
            if "Liabilities" in organized_company_financials.get(key).get(year).keys() and "StockholdersEquity" in organized_company_financials.get(key).get(year).keys():
                                        year_liabilities = organized_company_financials[key][year]["Liabilities"]
                                        year_stockholders_equity = organized_company_financials[key][year]["StockholdersEquity"]
                            
                                        debt_to_equity_ratio = year_liabilities / year_stockholders_equity
                                        
                                        print(key,year, "debt to equity ratio = " , debt_to_equity_ratio)
                                        
            if "NetIncomeLoss" in organized_company_financials.get(key).get(year).keys() and "Assets" in organized_company_financials.get(key).get(year).keys():
                                                    year_net_income_loss = organized_company_financials[key][year]["NetIncomeLoss"]
                                                    year_assets = organized_company_financials[key][year]["Assets"]
                                        
                                                    return_on_assets = year_net_income_loss / year_assets
                                                    
                                                    print(key,year, "return on assets ratio = " , return_on_assets)
            else: 
                print("Error", key ,"doesn't contain one of the values needed")
            
if __name__ == "__main__":
    main()