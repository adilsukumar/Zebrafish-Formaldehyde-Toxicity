"""Reproduce the report's exploratory control-corrected two-point probit calculation."""
from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path
from statistics import NormalDist


def abbott(response: float, control: float) -> float:
    if not 0 <= control < 1 or not 0 <= response <= 1:
        raise ValueError("Control must be in [0, 1); response must be in [0, 1]")
    return max(0.0, (response - control) / (1 - control))


def read_observations(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as handle:
        records = list(csv.DictReader(handle))
    if not records:
        raise ValueError("No observations")
    rows = []
    for record in records:
        row = {**record, "nominal_ppm": float(record["nominal_ppm"]), "exposed": int(record["exposed"]), "deaths": int(record["deaths"]), "duration_hours": float(record["duration_hours"])}
        if row["exposed"] <= 0 or not 0 <= row["deaths"] <= row["exposed"] or row["nominal_ppm"] < 0:
            raise ValueError("Invalid counts or nominal concentration")
        row["mortality"] = row["deaths"] / row["exposed"]
        rows.append(row)
    if sum(row["nominal_ppm"] == 0 for row in rows) != 1:
        raise ValueError("Exactly one control observation is required")
    if len({row["nominal_ppm"] for row in rows}) != len(rows):
        raise ValueError("This descriptive script expects one vessel per concentration")
    return rows


def two_point_crossing(concentrations: list[float], responses: list[float], upper: float = 0.975) -> dict:
    if len(concentrations) != 2 or len(responses) != 2:
        raise ValueError("Exactly two non-control exposure groups are required")
    if not 0.5 < upper < 1:
        raise ValueError("Finite upper endpoint must be between 0.5 and 1")
    if any(c <= 0 for c in concentrations) or concentrations[0] == concentrations[1]:
        raise ValueError("Concentrations must be positive and distinct")
    if any(not 0 < p <= 1 for p in responses):
        raise ValueError("Corrected responses must be in (0, 1]")
    finite = [upper if p == 1 else p for p in responses]
    xs = [math.log10(c) for c in concentrations]
    ys = [5 + NormalDist().inv_cdf(p) for p in finite]
    slope = (ys[1] - ys[0]) / (xs[1] - xs[0])
    if slope <= 0:
        raise ValueError("Responses must increase with concentration")
    intercept = ys[0] - slope * xs[0]
    return {"upper_endpoint_convention": upper, "intercept": intercept, "slope": slope, "descriptive_50_percent_crossing_nominal_ppm": 10 ** ((5 - intercept) / slope)}


def analyze(rows: list[dict]) -> dict:
    control = next(row for row in rows if row["nominal_ppm"] == 0)["mortality"]
    exposed = sorted((row for row in rows if row["nominal_ppm"] > 0), key=lambda row: row["nominal_ppm"])
    corrected = [abbott(row["mortality"], control) for row in exposed]
    concentrations = [row["nominal_ppm"] for row in exposed]
    return {
        "scope": "Exploratory adult zebrafish screening; one vessel per group, not a validated population LC50",
        "rows": rows,
        "control_mortality": control,
        "corrected_responses": corrected,
        "primary": two_point_crossing(concentrations, corrected, 0.975),
        "endpoint_sensitivity": two_point_crossing(concentrations, corrected, 0.95),
        "limitations": ["Two nonzero nominal concentrations", "No independent vessel replication", "No confidence interval estimated", "Concentrations were not analytically verified", "Life stage follows the final adult report; earlier draft embryo labels are superseded"],
    }


def write_svg(rows: list[dict], output: Path) -> None:
    bars = []
    for i, row in enumerate(rows):
        x, height = 100 + i * 155, row["mortality"] * 220
        bars.append(f'<rect x="{x}" y="{270-height}" width="80" height="{height}" fill="#236b75"/><text x="{x+40}" y="{255-height}" text-anchor="middle">{row["mortality"]:.0%}</text><text x="{x+40}" y="295" text-anchor="middle">{row["nominal_ppm"]:g} ppm</text>')
    output.write_text('<svg xmlns="http://www.w3.org/2000/svg" width="620" height="350" viewBox="0 0 620 350"><rect width="620" height="350" fill="white"/><g font-family="sans-serif" font-size="16" fill="#15252a"><text x="310" y="30" text-anchor="middle">Recorded 96-hour mortality (10 adults per group)</text><path d="M65 50V270H560" stroke="#15252a" fill="none"/>'+''.join(bars)+'<text x="310" y="335" text-anchor="middle">One vessel per group; descriptive observations</text></g></svg>', encoding="utf-8")


def main() -> None:
    root = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=root / "data/observations.csv")
    parser.add_argument("--output", type=Path, default=root / "results")
    args = parser.parse_args()
    rows = read_observations(args.data)
    summary = analyze(rows)
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    write_svg(rows, args.output / "mortality.svg")
    print(json.dumps({"primary_crossing_ppm": summary["primary"]["descriptive_50_percent_crossing_nominal_ppm"], "alternative_crossing_ppm": summary["endpoint_sensitivity"]["descriptive_50_percent_crossing_nominal_ppm"]}, indent=2))


if __name__ == "__main__":
    main()
