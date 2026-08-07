from config import JSON_OUTPUT_PATH
from curve_analysis import latest_curve, spread_summary
from data_fetch import fetch_curve_history
from export_json import write_json
from report import print_report


def main() -> None:
    df = fetch_curve_history()
    curve = latest_curve(df)
    spreads = spread_summary(df)
    curve_date = df["Date"].iloc[-1].strftime("%Y-%m-%d")

    print_report(curve_date, curve, spreads)
    write_json(curve_date, curve, spreads, JSON_OUTPUT_PATH)


if __name__ == "__main__":
    main()
