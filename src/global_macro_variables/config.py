"""All the general configuration of the project."""
from pathlib import Path

SRC = Path(__file__).parent.resolve()
BLD = SRC.joinpath("..", "..", "bld").resolve()

TEST_DIR = SRC.joinpath("..", "..", "tests").resolve()
PAPER_DIR = SRC.joinpath("..", "..", "paper").resolve()

TOP_DIR = SRC.joinpath("..", "..").resolve()


__all__ = ["BLD", "SRC", "TEST_DIR", "GROUPS"]


FRED_API_KEY = "a6c090d9708fcd388e74204168cc7f43"


FRED_INTEREST_RATE_SERIES = {
    "Japan": "IRLTLT01JPM156N",
    "Germany": "IRLTLT01DEM156N",
    "USA": "IRLTLT01USM156N",
    "United Kingdom": "IRLTLT01GBM156N",
    "India": "INDIRLTLT01STM",
    "Canada": "IRLTLT01CAM156N",
    "France": "IRLTLT01FRM156N",
    "Italy": "IRLTLT01ITM156N",
    "Australia": "IRLTLT01AUM156N",
    "Switzerland": "IRLTLT01CHM156N",
    "Spain": "IRLTLT01ESM156N",
    "Greece": "IRLTLT01GRM156N",
    "Mexico": "IRLTLT01MXM156N",
    "South Africa": "IRLTLT01ZAM156N",
    "South Korea": "IRLTLT01KRM156N",
    "Netherlands": "IRLTLT01NLM156N",
    "Sweden": "IRLTLT01SEM156N",
    "Ireland": "IRLTLT01IEM156N",
    "Belgium": "IRLTLT01BEM156N",
    "New Zealand": "IRLTLT01NZM156N",
    "Denmark": "IRLTLT01DKM156N",
    "Poland": "IRLTLT01PLM156N",
    "Luxembourg": "IRLTLT01LUM156N",
    "Norway": "IRLTLT01NOM156N",
    "Portugal": "IRLTLT01PTM156N",
    "Chile": "IRLTLT01CLM156N",
    "Austria": "IRLTLT01ATM156N",
    "Israel": "IRLTLT01ILM156N",
    "Hungary": "IRLTLT01HUM156N",
    "Russia": "IRLTLT01RUM156N",
    "Finland": "IRLTLT01FIM156N",
    "Colombia": "COLIRLTLT01STM",
    "Latvia": "LVAIRLTLT01STM",
    "Slovak Republic": "IRLTLT01SKM156N",
    "Costa Rica": "CRIIRLTLT01STM",
    "Slovenia": "IRLTLT01SIM156N",
    "Lithuania": "LTUIRLTLT01STM",
    "Czech Republic": "IRLTLT01CZM156N",
    "Iceland": "IRLTLT01ISM156N",
}


OECD_QUARTERLY_GDP_USD_XML_QUERY_LINK = "https://sdmx.oecd.org/public/rest/data/OECD.SDD.NAD,DSD_NAMAIN1@DF_QNA_EXPENDITURE_USD,1.0/Q...S1..B1GQ.....V..?dimensionAtObservation=AllDimensions"


OECD_QUARTERLY_DEBT_AS_PERCENT_GDP_QUERY_LINK = "https://sdmx.oecd.org/public/rest/data/OECD.SDD.NAD,DSD_NASEC20@DF_T7PSD_Q,1.0/Q....S13.....FD4.T.PT_B1GQ..N....INST?dimensionAtObservation=AllDimensions"


OECD_QUARTERLY_CURRENT_ACCOUNT_QUERY_LINK = "https://sdmx.oecd.org/public/rest/data/OECD.SDD.TPS,DSD_BOP@DF_BOP,1.0/..CA.B..Q.USD_EXC.N?dimensionAtObservation=AllDimensions"


OECD_REAL_QUARTERLY_GDP_QUERY_LINK = "https://sdmx.oecd.org/public/rest/data/OECD.SDD.NAD,DSD_NAMAIN1@DF_QNA_BY_ACTIVITY_OUTPUT,1.0/Q.N....B1G.._T...L..?dimensionAtObservation=AllDimensions"

EUROSTAT_CPI_QUARTERLY_QUERY_LINK = "https://sdmx.oecd.org/public/rest/data/OECD.SDD.TPS,DSD_PRICES@DF_PRICES_HICP,1.0/.M.HICP.CPI.PA._T.N.GY?dimensionAtObservation=AllDimensions"


OECD_DATA_QUERY_LINKS = {
    "debt_by_gdp.pkl": OECD_QUARTERLY_DEBT_AS_PERCENT_GDP_QUERY_LINK,
    "quarterly_gdp_USD.pkl": OECD_QUARTERLY_GDP_USD_XML_QUERY_LINK,
    "current_account.pkl": OECD_QUARTERLY_CURRENT_ACCOUNT_QUERY_LINK,
    "real_quarterly_gva.pkl": OECD_REAL_QUARTERLY_GDP_QUERY_LINK,
    "cpi.pkl": EUROSTAT_CPI_QUARTERLY_QUERY_LINK,
}


OECD_VARIABLE_NAMES = {
    "debt_by_gdp.pkl": "Public_Debt_as_%_of_GDP",
    "quarterly_gdp_USD.pkl": "GDP_in_USD_Current_Prices",
    "current_account.pkl": "Current_Account_in_USD",
    "real_quarterly_gva.pkl": "Real_Quarterly_GVA_in_Domestic_Currency",
    "cpi.pkl": "Eurostat_CPI_Annualised Growth_Rate",
}


COUNTRY_CODES_AND_NAMES_MAPPING = {
    "JPN": "Japan",
    "DEU": "Germany",
    "USA": "USA",
    "GBR": "United Kingdom",
    "IND": "India",
    "CAN": "Canada",
    "FRA": "France",
    "ITA": "Italy",
    "AUS": "Australia",
    "CHE": "Switzerland",
    "ESP": "Spain",
    "GRC": "Greece",
    "MEX": "Mexico",
    "ZAF": "South Africa",
    "KOR": "South Korea",
    "NLD": "Netherlands",
    "SWE": "Sweden",
    "IRL": "Ireland",
    "BEL": "Belgium",
    "NZL": "New Zealand",
    "DNK": "Denmark",
    "POL": "Poland",
    "LUX": "Luxembourg",
    "NOR": "Norway",
    "PRT": "Portugal",
    "CHL": "Chile",
    "AUT": "Austria",
    "ISR": "Israel",
    "HUN": "Hungary",
    "RUS": "Russia",
    "FIN": "Finland",
    "COL": "Colombia",
    "LVA": "Latvia",
    "SVK": "Slovak Republic",
    "CRI": "Costa Rica",
    "SVN": "Slovenia",
    "LTU": "Lithuania",
    "CZE": "Czech Republic",
    "ISL": "Iceland",
}
