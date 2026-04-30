import pandas as pd

def analyze_sales_drop(region: str, category: str) -> dict:
    df = pd.read_csv("data/sales.csv")
    filtered = df[(df["region"] == region) & (df["category"] == category)]

    if len(filtered) < 2:
        return {"error": "Not enough sales data"}

    filtered = filtered.sort_values("date")
    latest = filtered.iloc[-1]["sales"]
    previous = filtered.iloc[-2]["sales"]

    change_pct = round(((latest - previous) / previous) * 100, 2)

    return {
        "region": region,
        "category": category,
        "previous_sales": int(previous),
        "latest_sales": int(latest),
        "change_pct": change_pct
    }