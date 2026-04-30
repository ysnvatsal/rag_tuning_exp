# Agentic Retail Analytics Copilot

## Overview
This project is a production-style proof of concept for an Agentic Retail Analytics Copilot.

The system analyzes retail sales and inventory data to explain business performance changes, detect anomalies, and recommend actions. It is designed to simulate how an AI agent can support retail operations teams with data-driven decision making.

## Use Case
Example question:

Why did Cereal sales drop in Region A?

The copilot checks:
- Sales trend
- Inventory status
- Reorder flags
- Anomaly detection
- Business explanation

## Tech Stack
- Python
- FastAPI
- Pandas
- Pydantic
- pytest
- Uvicorn

## Architecture
User Request  
→ FastAPI Endpoint  
→ Retail Analytics Agent  
→ Sales Tool  
→ Inventory Tool  
→ Anomaly Detection Tool  
→ Structured Business Response

## Features
- Agent-style workflow
- Tool-based reasoning
- Sales drop analysis
- Inventory risk check
- Anomaly detection
- Structured JSON response
- Production-style folder structure

## Project Structure
```text
app/
  main.py
  agent.py
  schemas.py
  prompts.py

tools/
  sales_tool.py
  inventory_tool.py
  anomaly_tool.py

data/
  sales.csv
  inventory.csv

tests/
  test_tools.py