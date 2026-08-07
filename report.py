def print_report(curve_date: str, curve: list[dict], spreads: dict) -> None:
    print(f"U.S. Treasury par yield curve — {curve_date}")
    print()
    print(f"{'Tenor':<10}{'Rate':>8}")
    print("-" * 18)
    for point in curve:
        print(f"{point['tenor']:<10}{point['rate']:>7.2f}%")

    print()
    print(f"{'Spread':<10}{'Current':>10}{'Status':>14}")
    print("-" * 34)
    for data in spreads.values():
        status = "INVERTED" if data["inverted"] else "normal"
        current = data["current"]
        current_str = f"{current:+.2f}%" if current is not None else "n/a"
        print(f"{data['label']:<10}{current_str:>10}{status:>14}")
