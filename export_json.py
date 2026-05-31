"""
next·PnL — S&P 500 Momentum Screener
מייצא top10.json לאתר
"""

import json
import datetime

# ============================================================
# הכנס כאן את הפלט של הסקרינר שלך
# ============================================================
SCREENER_OUTPUT = [
    {"ticker": "ADBE", "price": 259.21, "target": 844.35, "upside": 225.74, "perf3m": -0.64, "fwd_pe": 9.8,  "ind_avg_pe": 32},
    {"ticker": "AES",  "price": 14.67,  "target": 47.78,  "upside": 225.67, "perf3m": 4.51,  "fwd_pe": 6.1,  "ind_avg_pe": 20},
    {"ticker": "CDW",  "price": 125.45, "target": 371.86, "upside": 196.42, "perf3m": 1.14,  "fwd_pe": 10.8, "ind_avg_pe": 32},
    {"ticker": "CPAY", "price": 361.80, "target": 979.39, "upside": 170.70, "perf3m": 8.97,  "fwd_pe": 11.8, "ind_avg_pe": 32},
    {"ticker": "CI",   "price": 277.40, "target": 736.79, "upside": 165.60, "perf3m": -4.10, "fwd_pe": 8.3,  "ind_avg_pe": 22},
    {"ticker": "ACN",  "price": 187.07, "target": 476.97, "upside": 154.97, "perf3m": -8.39, "fwd_pe": 12.6, "ind_avg_pe": 32},
    {"ticker": "BMY",  "price": 57.18,  "target": 135.76, "upside": 137.42, "perf3m": -7.33, "fwd_pe": 9.3,  "ind_avg_pe": 22},
    {"ticker": "BAX",  "price": 18.78,  "target": 44.36,  "upside": 136.22, "perf3m": -4.57, "fwd_pe": 9.3,  "ind_avg_pe": 22},
    {"ticker": "APTV", "price": 67.94,  "target": 149.92, "upside": 120.67, "perf3m": -6.25, "fwd_pe": 10.0, "ind_avg_pe": 22},
    {"ticker": "XYZ",  "price": 75.72,  "target": 159.36, "upside": 110.47, "perf3m": 17.49, "fwd_pe": 15.2, "ind_avg_pe": 32},
    {"ticker": "COF",  "price": 187.93, "target": 388.62, "upside": 106.79, "perf3m": -2.87, "fwd_pe": 7.7,  "ind_avg_pe": 16},
    {"ticker": "DAL",  "price": 82.48,  "target": 169.26, "upside": 105.21, "perf3m": 28.71, "fwd_pe": 10.2, "ind_avg_pe": 21},
    {"ticker": "ALL",  "price": 206.09, "target": 420.37, "upside": 103.98, "perf3m": -3.13, "fwd_pe": 7.8,  "ind_avg_pe": 16},
    {"ticker": "CCL",  "price": 28.06,  "target": 57.20,  "upside": 103.84, "perf3m": -3.12, "fwd_pe": 10.8, "ind_avg_pe": 22},
    {"ticker": "CVS",  "price": 90.98,  "target": 183.99, "upside": 102.23, "perf3m": 12.39, "fwd_pe": 10.9, "ind_avg_pe": 22},
]

def export_json(stocks, output_path="top10.json"):
    payload = {
        "run_date": datetime.date.today().isoformat(),
        "stocks": sorted(stocks, key=lambda x: x["upside"], reverse=True)
    }
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
    print(f"✅  Exported {len(stocks)} stocks → {output_path}")
    print(f"    Run date: {payload['run_date']}")

if __name__ == "__main__":
    export_json(SCREENER_OUTPUT)
