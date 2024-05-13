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

OECD_GOVERNMENT_REVENUE_LINK = "https://sdmx.oecd.org/public/rest/data/OECD.SDD.NAD,DSD_NASEC1@DF_QSA_TRANSACTIONS_C,1.0/Q.N..S13...OTR.......?dimensionAtObservation=AllDimensions"

EUROSTAT_CPI_QUARTERLY_QUERY_LINK = "https://sdmx.oecd.org/public/rest/data/OECD.SDD.TPS,DSD_PRICES@DF_PRICES_HICP,1.0/.M.HICP.CPI.PA._T.N.GY?dimensionAtObservation=AllDimensions"


OECD_DATA_QUERY_LINKS = {
    "debt_by_gdp.pkl": OECD_QUARTERLY_DEBT_AS_PERCENT_GDP_QUERY_LINK,
    "quarterly_gdp_USD.pkl": OECD_QUARTERLY_GDP_USD_XML_QUERY_LINK,
    "current_account.pkl": OECD_QUARTERLY_CURRENT_ACCOUNT_QUERY_LINK,
    "real_quarterly_gva.pkl": OECD_REAL_QUARTERLY_GDP_QUERY_LINK,
    "cpi.pkl": EUROSTAT_CPI_QUARTERLY_QUERY_LINK,
    "government_revenue.pkl": OECD_GOVERNMENT_REVENUE_LINK,
}


OECD_VARIABLE_NAMES = {
    "debt_by_gdp.pkl": "Public_Debt_as_%_of_GDP",
    "quarterly_gdp_USD.pkl": "GDP_in_USD_Current_Prices",
    "current_account.pkl": "Current_Account_in_USD",
    "real_quarterly_gva.pkl": "Real_Quarterly_GVA_in_Domestic_Currency",
    "cpi.pkl": "Eurostat_CPI_Annualised Growth_Rate",
    "government_revenue.pkl": "Government_Revenue_in_Domestic_Currency",
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

COUNTRY_MAPPING_RATING_DATA_VS_OECD_DATA_FOR_MERGING = {
    "colombia": "Colombia",
    "costa rica": "Costa Rica",
    "netherlands": "Netherlands",
    "chile": "Chile",
    "latvia": "Latvia",
    "united kingdom": "United Kingdom",
    "denmark": "Denmark",
    "luxembourg": "Luxembourg",
    "austria": "Austria",
    "new zealand": "New Zealand",
    "australia": "Australia",
    "israel": "Israel",
    "italy": "Italy",
    "finland": "Finland",
    "norway": "Norway",
    "slovenia": "Slovenia",
    "lithuania": "Lithuania",
    "india": "India",
    "slovak republic": "Slovak Republic",
    "greece": "Greece",
    "hungary": "Hungary",
    "portugal": "Portugal",
    "iceland": "Iceland",
    "spain": "Spain",
    "germany": "Germany",
    "switzerland": "Switzerland",
    "japan": "Japan",
    "belgium": "Belgium",
    "sweden": "Sweden",
    "canada": "Canada",
    "ireland": "Ireland",
    "usa": "USA",
    "mexico": "Mexico",
    "france": "France",
    "russia": "Russia",
    "czech republic": "Czech Republic",
    "south korea": "South Korea",
    "south africa": "South Africa",
    "poland": "Poland",
}

COUNTRY_TABLE_ID_FOR_MOODY_RATING = {
    "colombia": "tb0_867",
    "costa rica": "tb0_868",
    "netherlands": "tb0_878",
    "chile": "tb0_865",
    "latvia": "tb0_885",
    "united kingdom": "tb0_849",
    "denmark": "tb0_870",
    "luxembourg": "tb0_887",
    "austria": "tb0_859",
    "new zealand": "tb0_892",
    "australia": "tb0_858",
    "israel": "tb0_884",
    "italy": "tb0_851",
    "finland": "tb0_876",
    "norway": "tb0_891",
    "slovenia": "tb0_873",
    "lithuania": "tb0_886",
    "india": "tb0_880",
    "slovak republic": "tb0_872",
    "greece": "tb0_877",
    "hungary": "tb0_879",
    "portugal": "tb0_852",
    "iceland": "tb0_883",
    "spain": "tb0_847",
    "germany": "tb0_848",
    "switzerland": "tb0_854",
    "japan": "tb0_855",
    "belgium": "tb0_860",
    "sweden": "tb0_900",
    "canada": "tb0_864",
    "ireland": "tb0_882",
    "usa": "tb0_853",
    "mexico": "tb0_890",
    "france": "tb0_850",
    "russia": "tb0_897",
    "czech republic": "tb0_895",
    "south korea": "tb0_1232",
    "south africa": "tb0_899",
    "poland": "tb0_894",
}


COUNTRY_URL_FOR_RATINGS_DICTIONARY = {
    "colombia": "colombia",
    "costa rica": "costa-rica",
    "netherlands": "netherlands",
    "chile": "chile",
    "latvia": "latvia",
    "united kingdom": "uk",
    "denmark": "denmark",
    "luxembourg": "luxembourg",
    "austria": "austria",
    "new zealand": "new-zealand",
    "australia": "australia",
    "israel": "israel",
    "italy": "italy",
    "finland": "finland",
    "norway": "norway",
    "slovenia": "slovenia",
    "lithuania": "lithuania",
    "india": "india",
    "slovak republic": "slovakia",
    "greece": "greece",
    "hungary": "hungary",
    "portugal": "portugal",
    "iceland": "iceland",
    "spain": "spain",
    "germany": "germany",
    "switzerland": "switzerland",
    "japan": "japan",
    "belgium": "belgium",
    "sweden": "sweden",
    "canada": "canada",
    "ireland": "ireland",
    "usa": "usa",
    "mexico": "mexico",
    "france": "france",
    "russia": "russia",
    "czech republic": "czech-republic",
    "south korea": "south-korea",
    "south africa": "south-africa",
    "poland": "poland",
}
