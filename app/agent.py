from tools.sales_tool import analyze_sales_drop
from tools.inventory_tool import check_inventory
from tools.anomaly_tool import detect_anomaly


class RetailAnalyticsAgent:
    def run(self, region: str, category: str) -> dict:
        sales_result = analyze_sales_drop(region, category)
        inventory_result = check_inventory(region, category)

        change_pct = sales_result.get("change_pct", 0)
        anomaly_result = detect_anomaly(change_pct)

        if inventory_result.get("reorder_flag") == "yes":
            likely_cause = "Inventory shortage likely contributed to the sales decline."
        elif anomaly_result.get("is_anomaly"):
            likely_cause = "Sales movement appears anomalous and needs further investigation."
        else:
            likely_cause = "Sales change appears within normal business variation."

        return {
            "summary": f"{category} sales in {region} changed by {change_pct}%.",
            "evidence": [
                {"tool_name": "sales_tool", "result": sales_result},
                {"tool_name": "inventory_tool", "result": inventory_result},
                {"tool_name": "anomaly_tool", "result": anomaly_result},
            ],
            "likely_cause": likely_cause,
            "recommended_action": "Review replenishment status, validate demand trend, and monitor next sales cycle."
        }