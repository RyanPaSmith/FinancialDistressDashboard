from src.services import all_company_financial_dataframes
from src.dictionary import financial_tags


def organize_company_financials_by_year():

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

    return organized_company_financials