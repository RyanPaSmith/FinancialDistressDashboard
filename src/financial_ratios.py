
""" 
================================================= 
Helper Function to check for divide by 0 on denominator. If denominator is 0 it does no work and returns None.
=================================================
"""

def safe_divide(numerator, denominator):
    if numerator is None or denominator is None or denominator == 0:
        return None

    return numerator / denominator

""" 
================================================= 
Calculates all financial ratios based on year by year organized data taken from organize_financials.py.
=================================================
"""

def calculate_financial_ratios(organized_company_financials):
    
    all_calculated_financial_ratios = []   
                     
    for key in organized_company_financials:
        
        for year in organized_company_financials[key]:

            year_data = organized_company_financials[key][year]
        
            assets = year_data.get("Assets")
            current_assets = year_data.get("AssetsCurrent")
            liabilities = year_data.get("Liabilities")
            current_liabilities = year_data.get("LiabilitiesCurrent")
            equity = year_data.get("StockholdersEquity")
            net_income = year_data.get("NetIncomeLoss")

            ratios = {}

            ratios["current ratio"] = safe_divide(current_assets, current_liabilities)
            ratios["debt to assets"] = safe_divide(liabilities, assets)
            ratios["debt to equity"] = safe_divide(liabilities, equity)
            ratios["return on assets"] = safe_divide(net_income, assets)

            if current_assets is not None and current_liabilities is not None:
                working_capital = current_assets - current_liabilities
            else:
                working_capital = None

            ratios["working capital"] = working_capital
            ratios["equity ratio"] = safe_divide(equity, assets)
            ratios["return on equity"] = safe_divide(net_income, equity)
            ratios["working capital to assets"] = safe_divide(working_capital, assets)
            ratios["net income to liabilities"] = safe_divide(net_income, liabilities)

            calculated_financial_ratios = {
            "ticker": key,
            "year": year,
            "ratios": ratios
            }

            all_calculated_financial_ratios.append(calculated_financial_ratios)
            
    return all_calculated_financial_ratios

            
    