# FastAPI Excel Processor


FastAPI Excel Processor 📊 + Streamlit UI 🌐
This project provides a web-based interface and REST API to interact with Excel files using FastAPI and Streamlit. It reads a given Excel sheet, lists the available tables (sheets), displays row names, and calculates the sum of numeric values in a selected row



FastAPI_Excel_Processor/
├── Data/
│   └── capbudg.xls             # <-- Place your Excel file here
├── main.py                     # FastAPI backend
├── streamlit_app.py            # Streamlit frontend
├── requirements.txt            # Dependencies
├── FastAPI_Excel.postman_collection.json
└── README.md                   # You're here



## Overview
A FastAPI app that processes an Excel file to:
- List sheet names
- Return row names from a sheet
- Compute the sum of numeric values in a row




## Endpoints
- `GET /list_tables`: Lists all sheet names.
- `GET /get_table_details?table_name=...`: Returns row labels.
- `GET /row_sum?table_name=...&row_name=...`: Returns sum of numeric values.

## How to Run
```bash
pip install -r requirements.txt
uvicorn main:app --reload --port 9090
```

## Make sure yout FastAPI app (main.py) is running
## In separate terminal ,run streamlit
```bash
streamlit run app.py
```