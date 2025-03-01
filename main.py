from fetch_data import get_option_data
from export_excel import save_to_excel

if __name__ == "__main__":
    stock_name = input("Enter Stock Symbol: ").upper()
    
    ce, pe = get_option_data(stock_name)

    if ce is not None and pe is not None:
        save_to_excel(stock_name, ce, pe)
