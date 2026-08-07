import pandas as pd

from config import SPREAD_PAIRS, TENOR_YEARS


def latest_curve(df: pd.DataFrame) -> list[dict]:
    """Today's full curve as (tenor, maturity-in-years, rate) points, in
    maturity order, skipping any tenor without a published rate.
    """
    latest_row = df.iloc[-1]
    curve = []
    for tenor, years in TENOR_YEARS.items():
        rate = latest_row.get(tenor)
        if pd.notna(rate):
            curve.append({"tenor": tenor, "years": years, "rate": float(rate)})
    return sorted(curve, key=lambda p: p["years"])


def _tenor_short_label(tenor: str) -> str:
    return tenor.replace(" Yr", "Y").replace(" Mo", "M").replace(" Month", "M")


def spread_summary(df: pd.DataFrame) -> dict:
    """For each configured pair: current spread (long - short), whether
    it's currently inverted, and the full history for charting.
    """
    result = {}
    for key, short_col, long_col in SPREAD_PAIRS:
        series = df[long_col] - df[short_col]
        history = [
            {"date": d.strftime("%Y-%m-%d"), "value": round(float(v), 3)}
            for d, v in zip(df["Date"], series)
            if pd.notna(v)
        ]
        current = history[-1]["value"] if history else None

        result[key] = {
            "label": f"{_tenor_short_label(short_col)}-{_tenor_short_label(long_col)}",
            "current": current,
            "inverted": current is not None and current < 0,
            "history": history,
        }
    return result
