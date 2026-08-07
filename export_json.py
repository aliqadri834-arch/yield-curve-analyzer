import json
from datetime import datetime, timezone
from pathlib import Path


def write_json(curve_date: str, curve: list[dict], spreads: dict, path: str) -> None:
    payload = {
        "generated_at": datetime.now(timezone.utc)
        .isoformat(timespec="seconds")
        .replace("+00:00", "Z"),
        "curve_date": curve_date,
        "curve": curve,
        "spreads": spreads,
    }

    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w") as f:
        json.dump(payload, f, indent=2)
        f.write("\n")
