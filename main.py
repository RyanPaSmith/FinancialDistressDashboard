from src.services import all_company_financial_dataframes


def main():
    for key in all_company_financial_dataframes:
        # print(key)

        company_financial_dataframes = all_company_financial_dataframes.get(key)

        asset_dataframe = company_financial_dataframes.get("Assets")
        current_asset_dataframe = company_financial_dataframes.get("AssetsCurrent")
        liability_dataframe = company_financial_dataframes.get("Liabilities")
        current_liabilities_dataframe = company_financial_dataframes.get("LiabilitiesCurrent")
        stockholders_equity_dataframe = company_financial_dataframes.get("StockholdersEquity")
        net_income_loss_dataframe = company_financial_dataframes.get("NetIncomeLoss")

        # """
        # ================================================= 
        # Current Ratio Calculation 
        # =================================================
        # """
        # # Returns about 15 billion in for current_ratio of Apple, 70 Billion for Microsoft and 7 million for Tesla
        # # This is just the mean value and should be done by row values per year
        # print(current_asset_dataframe["val"].mean() - current_liabilities_dataframe["val"].mean())

        # """
        # ================================================= 
        # Debt-Equity Ratio 
        # =================================================
        # """

        # # Returns 259.36 billion for Apple, 268.55 billion for Microsoft, 40.17 billion for Tesla
        # # This is just the mean value and should be done by row values per year
        # print(liability_dataframe["val"].mean() + stockholders_equity_dataframe["val"].mean())


if __name__ == "__main__":
    main()