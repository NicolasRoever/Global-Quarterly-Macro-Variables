"""All the general configuration of the project."""
from pathlib import Path

SRC = Path(__file__).parent.resolve()
BLD = SRC.joinpath("..", "..", "bld").resolve()

TEST_DIR = SRC.joinpath("..", "..", "tests").resolve()
PAPER_DIR = SRC.joinpath("..", "..", "paper").resolve()


__all__ = ["BLD", "SRC", "TEST_DIR", "GROUPS"]



FRED_API_KEY = "a6c090d9708fcd388e74204168cc7f43"


FRED_INTEREST_RATE_SERIES = {
    "Japan":"IRLTLT01JPM156N",
    "Germany":"IRLTLT01DEM156N",
    "USA":"IRLTLT01USM156N",
    "United Kingdom": "IRLTLT01GBM156N",
    "India": "INDIRLTLT01STM",
    "Canada":"IRLTLT01CAM156N", 
    "France":"IRLTLT01FRM156N", 
    "Italy":"IRLTLT01ITM156N", 
    "Australia":"IRLTLT01AUM156N",
    "Switzerland":"IRLTLT01CHM156N",
    "Spain":"IRLTLT01ESM156N",
    "Greece":"IRLTLT01GRM156N",
    "Mexico":"IRLTLT01MXM156N",
    "South Africa":"IRLTLT01ZAM156N",
    "South Korea":"IRLTLT01KRM156N", 
    "Netherlands":"IRLTLT01NLM156N",
    "Sweden":"IRLTLT01SEM156N",
    "Ireland":"IRLTLT01IEM156N",
    "Belgium":"IRLTLT01BEM156N", 
    "New Zealand":"IRLTLT01NZM156N", 
    "Denmark":"IRLTLT01DKM156N", 
    "Poland": "IRLTLT01PLM156N", 
    "Luxembourg":"IRLTLT01LUM156N", 
    "Norway":"IRLTLT01NOM156N", 
    "Portugal":"IRLTLT01PTM156N", 
    "Chile":"IRLTLT01CLM156N", 
    "Austria":"IRLTLT01ATM156N", 
    "Israel":"IRLTLT01ILM156N", 
    "Hungary":"IRLTLT01HUM156N",
    "Russia":"IRLTLT01RUM156N", 
    "Finland":"IRLTLT01FIM156N", 
    "Colombia":"COLIRLTLT01STM", 
    "Latvia":"LVAIRLTLT01STM", 
    "Slovak Republic":"IRLTLT01SKM156N", 
    "Costa Rica":"CRIIRLTLT01STM",
    "Slovenia":"IRLTLT01SIM156N",
    "Lithuania":"LTUIRLTLT01STM", 
    "Czech Republic":"IRLTLT01CZM156N",
    "Iceland":"IRLTLT01ISM156N"
    }









OECD_QUARTERLY_GDP_USD_XML_QUERY_LINK = "https://sdmx.oecd.org/public/rest/data/OECD.SDD.NAD,DSD_NAMAIN1@DF_QNA_EXPENDITURE_USD,1.0/Q...S1..B1GQ.....V..?dimensionAtObservation=AllDimensions"


OECD_QUARTERLY_DEBT_AS_PERCENT_GDP_QUERY_LINK = "https://sdmx.oecd.org/public/rest/data/OECD.SDD.NAD,DSD_NASEC20@DF_T7PSD_Q,1.0/Q....S13.....FD4.T.PT_B1GQ......?dimensionAtObservation=AllDimensions"


OECD_QUARTERLY_CURRENT_ACCOUNT_QUERY_LINK = "https://sdmx.oecd.org/public/rest/data/OECD.SDD.TPS,DSD_BOP@DF_BOP,1.0/..CA.B..Q.USD_EXC.N?dimensionAtObservation=AllDimensions"


OECD_REAL_QUARTERLY_GDP_QUERY_LINK = "https://sdmx.oecd.org/public/rest/data/OECD.SDD.NAD,DSD_NAMAIN1@DF_QNA_BY_ACTIVITY_OUTPUT,1.0/Q.N....B1G.._T...L..?dimensionAtObservation=AllDimensions"

EUROSTAT_CPI_QUARTERLY_QUERY_LINK = "https://sdmx.oecd.org/public/rest/data/OECD.SDD.TPS,DSD_PRICES@DF_PRICES_HICP,1.0/.M.HICP.CPI.PA._T.N.GY?dimensionAtObservation=AllDimensions"


