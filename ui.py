import streamlit as st
from data_processing import fetch_options_data
import pandas as pd

st.title("FNO Options Analyzer")

symbol = st.text_input("Enter Stock Symbol:", "AAPL")

if st.button("Fetch Data"):
    calls, puts = fetch_options_data(symbol)
    
    if calls is not None and puts is not None:
        st.subheader("Call Options Data")
        st.dataframe(calls)
        
        st.subheader("Put Options Data")
        st.dataframe(puts)

        if st.button("Download Excel"):
            with pd.ExcelWriter(f"{symbol}_options.xlsx") as writer:
                calls.to_excel(writer, sheet_name="Call Options", index=False)
                puts.to_excel(writer, sheet_name="Put Options", index=False)
            st.success(f"File saved as {symbol}_options.xlsx")
