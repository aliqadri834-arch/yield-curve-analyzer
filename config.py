# U.S. Treasury daily par yield curve rates -- public CSV, no key needed.
# One file per calendar year; most recent date first within each file.
TREASURY_CSV_URL_TEMPLATE = (
    "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/"
    "daily-treasury-rates.csv/{year}/all?type=daily_treasury_yield_curve"
    "&field_tdr_date_value={year}&page&_format=csv"
)

# How many prior calendar years (beyond the current one) to pull, so the
# historical spread chart has enough runway. 1 = current year + last year.
HISTORY_YEARS_BACK = 1

# Maturity in years for each tenor column in the CSV -- needed to place
# points correctly on a yield-curve chart, since tenors aren't evenly
# spaced (1Mo-2Mo is a month apart; 10Yr-20Yr is a decade apart).
TENOR_YEARS = {
    "1 Mo": 1 / 12,
    "1.5 Month": 1.5 / 12,
    "2 Mo": 2 / 12,
    "3 Mo": 3 / 12,
    "4 Mo": 4 / 12,
    "6 Mo": 6 / 12,
    "1 Yr": 1,
    "2 Yr": 2,
    "3 Yr": 3,
    "5 Yr": 5,
    "7 Yr": 7,
    "10 Yr": 10,
    "20 Yr": 20,
    "30 Yr": 30,
}

# (id, short tenor, long tenor). Spread = long - short; negative = inverted.
SPREAD_PAIRS = [
    ("2yr10yr", "2 Yr", "10 Yr"),
    ("3mo10yr", "3 Mo", "10 Yr"),
]

JSON_OUTPUT_PATH = "data/curve.json"
