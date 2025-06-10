import streamlit as st
import requests

BASE_URL = "http://localhost:9090"

st.title(" FastAPI Excel Processor (UI)")

try:
    list_tables_resp = requests.get(f"{BASE_URL}/list_tables")
    list_tables_resp.raise_for_status()
    tables = list_tables_resp.json().get("tables", [])
except Exception as e:
    st.error(f"Could not fetch table list: {e}")
    st.stop()


table_name = st.selectbox("Select a table", tables)

if table_name:
    try:
        row_resp = requests.get(f"{BASE_URL}/get_table_details", params={"table_name": table_name})
        row_resp.raise_for_status()
        row_names = row_resp.json().get("row_names", [])
    except Exception as e:
        st.error(f"Failed to load row names: {e}")
        st.stop()

    row_name = st.selectbox("Select a row to sum", row_names)

 
    if row_name:
        try:
            sum_resp = requests.get(f"{BASE_URL}/row_sum", params={
                "table_name": table_name,
                "row_name": row_name
            })
            sum_resp.raise_for_status()
            row_sum = sum_resp.json().get("sum", "N/A")

            st.success(f"Sum of '{row_name}' in '{table_name}': {row_sum}")
        except Exception as e:
            st.error(f"Failed to fetch sum: {e}")
