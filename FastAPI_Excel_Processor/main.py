from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import os

app = FastAPI(title="FastAPI Excel Processor")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXCEL_FILE_PATH = os.path.join(BASE_DIR, "Data/capbudg.xls")

try:
    excel_data = pd.read_excel(EXCEL_FILE_PATH, sheet_name=None)
except Exception as e:
    raise RuntimeError(f"Failed to load Excel file: {e}")

@app.get("/list_tables")
def list_tables():
    return {"tables": list(excel_data.keys())}

@app.get("/get_table_details")
def get_table_details(table_name: str = Query(...)):
    if table_name not in excel_data:
        raise HTTPException(status_code=404, detail="Table not found")
    df = excel_data[table_name]
    first_col = df.columns[0]
    row_names = df[first_col].dropna().astype(str).tolist()
    return {
        "table_name": table_name,
        "row_names": row_names
    }

@app.get("/row_sum")
def row_sum(table_name: str = Query(...), row_name: str = Query(...)):
    if table_name not in excel_data:
        raise HTTPException(status_code=404, detail="Table not found")
    df = excel_data[table_name]
    first_col = df.columns[0]
    row = df[df[first_col].astype(str) == row_name]
    if row.empty:
        raise HTTPException(status_code=404, detail="Row not found")
    numeric_data = row.iloc[0, 1:]
    numeric_sum = pd.to_numeric(numeric_data, errors='coerce').sum()
    return {
        "table_name": table_name,
        "row_name": row_name,
        "sum": float(numeric_sum)
    }