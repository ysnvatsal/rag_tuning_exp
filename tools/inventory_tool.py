import pandas as pd

def check_inventory(region: str, category: str) -> dict:
    df = pd.read_csv("data/inventory.csv")
    filtered = df[(df["region"] == region) & (df["category"] == category)]

    if filtered.empty:
        return {"error": "No inventory data found"}

    latest = filtered.sort_values("date").iloc[-1]

    return {
        "region": region,
        "category": category,
        "stock_level": int(latest["stock_level"]),
        "reorder_flag": str(latest["reorder_flag"])
    }