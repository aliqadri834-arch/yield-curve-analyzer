from datetime import date

import pandas as pd

from config import HISTORY_YEARS_BACK, TREASURY_CSV_URL_TEMPLATE


def fetch_year(year: int) -> pd.DataFrame:
    """Pull one calendar year of daily par yield curve rates."""
    url = TREASURY_CSV_URL_TEMPLATE.format(year=year)
    df = pd.read_csv(url)
    if df.empty:
        raise ValueError(f"no data returned for {year}")
    df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y")
    return df


def fetch_curve_history(years_back: int = HISTORY_YEARS_BACK) -> pd.DataFrame:
    """Current year plus `years_back` prior years, concatenated and sorted
    oldest-to-newest (Treasury's own files are newest-first).
    """
    current_year = date.today().year
    years = [current_year - i for i in range(years_back + 1)]
    frames = [fetch_year(y) for y in years]
    combined = pd.concat(frames, ignore_index=True)
    return combined.sort_values("Date").reset_index(drop=True)
