import streamlit as st
from fetch_data import get_option_data
from export_excel import save_to_excel

st.title("Options Data Tracker")

stock_name = st.text_input("Enter Stock Symbol:", "AAPL").upper()

if st.button("Fetch Data"):
    ce, pe = get_option_data(stock_name)
    if ce is not None and pe is not None:
        save_to_excel(stock_name, ce, pe)
        st.success(f"Excel file saved as {stock_name}_OI_Data.xlsx")
        st.dataframe(ce)  # Display CE Data
        st.dataframe(pe)  # Display PE Data
