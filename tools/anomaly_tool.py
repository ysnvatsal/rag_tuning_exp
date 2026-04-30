def detect_anomaly(change_pct: float) -> dict:
    is_anomaly = bool(abs(change_pct) >= 25)

    return {
        "is_anomaly": is_anomaly,
        "reason": "Sales changed more than 25%" if is_anomaly else "Sales change is within normal range"
    }