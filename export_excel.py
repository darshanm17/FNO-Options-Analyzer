import pandas as pd

def save_to_excel(stock, ce_data, pe_data):
    with pd.ExcelWriter(f"{stock}_OI_Data.xlsx") as writer:
        ce_data.to_excel(writer, sheet_name="Call Options", index=False)
        pe_data.to_excel(writer, sheet_name="Put Options", index=False)
    print(f"Excel file saved as {stock}_OI_Data.xlsx")
