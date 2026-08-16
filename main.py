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
    
    all_calculated_financial_ratios = []   
             
    for key in organized_company_financials:
        
        for year in organized_company_financials[key]:
            
            calculated_financial_ratios = {}
            ratios = {}     
            
            """ 
            ================================================= 
            Calculate Current Ratio
            =================================================
            """
            
            if "AssetsCurrent" in organized_company_financials.get(key).get(year).keys() and "LiabilitiesCurrent" in organized_company_financials.get(key).get(year).keys():
                
                year_current_assets = organized_company_financials[key][year]["AssetsCurrent"]
                year_current_liabilities = organized_company_financials[key][year]["LiabilitiesCurrent"]
    
                current_ratio = year_current_assets / year_current_liabilities
                calculated_financial_ratios.update({"ticker" : key , "year" : year, "ratios" : ratios})
                ratios["current ratio"] = current_ratio
                
            else : 
                
                calculated_financial_ratios.update({"ticker" : key , "year" : year, "ratios" : ratios})
                ratios["current ratio"] = None
                
            # print(calculated_financial_ratios)
            
            
            """ 
            ================================================= 
            Calculate Debt-to-Assets Ratio
            =================================================
            """
            
            if "Liabilities" in organized_company_financials.get(key).get(year).keys() and "Assets" in organized_company_financials.get(key).get(year).keys():
                
                year_assets = organized_company_financials[key][year]["Assets"]
                year_liabilities = organized_company_financials[key][year]["Liabilities"]
                
                debt_to_assets_ratio = year_liabilities / year_assets
                            
                calculated_financial_ratios.update({"ticker" : key , "year" : year, "ratios" : ratios})
                ratios["debt to assets"] = debt_to_assets_ratio
                               
            else: 
                               
                calculated_financial_ratios.update({"ticker" : key , "year" : year, "ratios" : ratios})
                ratios["debt to assets"] = None
                
            # print(calculated_financial_ratios)
                
            """ 
            ================================================= 
            Calculate Debt-to-Equity Ratio
            =================================================
            """
                         
            if "Liabilities" in organized_company_financials.get(key).get(year).keys() and "StockholdersEquity" in organized_company_financials.get(key).get(year).keys():
                
                year_liabilities = organized_company_financials[key][year]["Liabilities"]
                year_stockholders_equity = organized_company_financials[key][year]["StockholdersEquity"]
                            
                debt_to_equity_ratio = year_liabilities / year_stockholders_equity
                                        
                calculated_financial_ratios.update({"ticker" : key , "year" : year, "ratios" : ratios})
                ratios["debt to equity"] = debt_to_equity_ratio
                                               
            else: 
                                               
                calculated_financial_ratios.update({"ticker" : key , "year" : year, "ratios" : ratios})
                ratios["debt to equity"] = None
                
            # print(calculated_financial_ratios)
                                        
                                        
            """ 
            ================================================= 
            Calculate Return on Assets Ratio
            =================================================
            """                    
                                        
            if "NetIncomeLoss" in organized_company_financials.get(key).get(year).keys() and "Assets" in organized_company_financials.get(key).get(year).keys():
                
                year_net_income_loss = organized_company_financials[key][year]["NetIncomeLoss"]
                year_assets = organized_company_financials[key][year]["Assets"]
                                        
                return_on_assets = year_net_income_loss / year_assets
                
                calculated_financial_ratios.update({"ticker" : key , "year" : year, "ratios" : ratios})
                ratios["return on assets"] = return_on_assets
                                              
            else: 
                                              
                calculated_financial_ratios.update({"ticker" : key , "year" : year, "ratios" : ratios})
                ratios["return on assets"] = None
                
            # print(calculated_financial_ratios)
            
            
            """ 
            ================================================= 
            Calculate Working Capital Ratio
            =================================================
            """                    
                                                    
            if "AssetsCurrent" in organized_company_financials.get(key).get(year).keys() and "LiabilitiesCurrent" in organized_company_financials.get(key).get(year).keys():
                            
                year_current_assets = organized_company_financials[key][year]["AssetsCurrent"]
                year_current_liabilities = organized_company_financials[key][year]["LiabilitiesCurrent"]
                                                    
                working_Capital = year_current_assets - year_current_liabilities
                            
                calculated_financial_ratios.update({"ticker" : key , "year" : year, "ratios" : ratios})
                ratios["working capital"] = working_Capital
                                               
            else: 
                                               
                calculated_financial_ratios.update({"ticker" : key , "year" : year, "ratios" : ratios})
                ratios["working capital"] = None
                
            # print(calculated_financial_ratios)
            
            """ 
            ================================================= 
            Calculate Equity Ratio
            =================================================
            """                    
                                                            
            if "Assets" in organized_company_financials.get(key).get(year).keys() and "StockholdersEquity" in organized_company_financials.get(key).get(year).keys():
                                    
                year_assets = organized_company_financials[key][year]["Assets"]
                year_stockholders_equity = organized_company_financials[key][year]["StockholdersEquity"]
                                                            
                equity_ratio = year_stockholders_equity / year_assets
                                    
                calculated_financial_ratios.update({"ticker" : key , "year" : year, "ratios" : ratios})
                ratios["equity ratio"] = equity_ratio
                                               
            else: 
                                               
                calculated_financial_ratios.update({"ticker" : key , "year" : year, "ratios" : ratios})
                ratios["equity ratio"] = None
                
            # print(calculated_financial_ratios)
            
            """ 
            ================================================= 
            Calculate Return on Equity Ratio
            =================================================
            """                    
                                                                        
            if "NetIncomeLoss" in organized_company_financials.get(key).get(year).keys() and "StockholdersEquity" in organized_company_financials.get(key).get(year).keys():
                                                
                year_net_income_loss = organized_company_financials[key][year]["NetIncomeLoss"]
                year_stockholders_equity = organized_company_financials[key][year]["StockholdersEquity"]
                                                                        
                return_on_equity = year_net_income_loss / year_stockholders_equity
                                                
                calculated_financial_ratios.update({"ticker" : key , "year" : year, "ratios" : ratios})
                ratios["return on equity"] = return_on_equity
                                                           
            else: 
                                                           
                calculated_financial_ratios.update({"ticker" : key , "year" : year, "ratios" : ratios})
                ratios["return on equity"] = None
                
            # print(calculated_financial_ratios)
            
            
            """ 
            ================================================= 
            Calculate Profit to Liabilities Ratio
            =================================================
            """                    
                                                                                    
            if "NetIncomeLoss" in organized_company_financials.get(key).get(year).keys() and "Liabilities" in organized_company_financials.get(key).get(year).keys():
                                                            
                year_net_income_loss = organized_company_financials[key][year]["NetIncomeLoss"]
                year_liabilities = organized_company_financials[key][year]["Liabilities"]
                                                                                    
                profit_to_liabilities = year_net_income_loss / year_liabilities
                                                            
                calculated_financial_ratios.update({"ticker" : key , "year" : year, "ratios" : ratios})
                ratios["profit to liabilities"] = profit_to_liabilities
                                                                       
            else: 
                                                                       
                calculated_financial_ratios.update({"ticker" : key , "year" : year, "ratios" : ratios})
                ratios["profit to liabilities"] = None
                            
            # print(calculated_financial_ratios)
            
            
            
            """ 
            ================================================= 
            Calculate Working Capital to Assets Ratio
            =================================================
            """                    
                                                                                                
            if "AssetsCurrent" in organized_company_financials.get(key).get(year).keys() and "LiabilitiesCurrent" in organized_company_financials.get(key).get(year).keys() and "Assets" in organized_company_financials.get(key).get(year).keys():
                                                                        
                year_current_assets = organized_company_financials[key][year]["AssetsCurrent"]
                year_current_liabilities = organized_company_financials[key][year]["LiabilitiesCurrent"]
                year_assets = organized_company_financials[key][year]["Assets"]
                                                                                                
                working_capital_to_assets = (year_current_assets - year_current_liabilities) / year_assets
                                                                        
                calculated_financial_ratios.update({"ticker" : key , "year" : year, "ratios" : ratios})
                ratios["working capital to assets"] = working_capital_to_assets
                                                                                   
            else: 
                                                                                   
                calculated_financial_ratios.update({"ticker" : key , "year" : year, "ratios" : ratios})
                ratios["working capital to assets"] = None
                                        
            # print(calculated_financial_ratios)
            
            """ 
            ================================================= 
            Calculate Net Income to Liabilities Ratio
            =================================================
            """                    
                                                                                                            
            if "NetIncomeLoss" in organized_company_financials.get(key).get(year).keys() and "Liabilities" in organized_company_financials.get(key).get(year).keys():
                                                                                    
                year_net_income_loss = organized_company_financials[key][year]["NetIncomeLoss"]
                year_liabilities = organized_company_financials[key][year]["Liabilities"]
                                                                                 
                net_income_to_liabilities = year_net_income_loss / year_liabilities
                                                                                    
                calculated_financial_ratios.update({"ticker" : key , "year" : year, "ratios" : ratios})
                ratios["net income to liabilities"] = net_income_to_liabilities
                                                                                               
            else: 
                                                                                               
                calculated_financial_ratios.update({"ticker" : key , "year" : year, "ratios" : ratios})
                ratios["net income to liabilities"] = None
                                                    
            # print(calculated_financial_ratios)
            
            all_calculated_financial_ratios.append(calculated_financial_ratios)
            
            print(all_calculated_financial_ratios)
                  
if __name__ == "__main__":
    main()