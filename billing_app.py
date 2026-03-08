import streamlit as st
import gspread
import pandas as pd
from google.oauth2.service_account import Credentials
#connect spread sheet
scope = [
"https://www.googleapis.com/auth/spreadsheets",
"https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_file(
"credentials.json",
scopes=scope
)

client = gspread.authorize(creds)

spreadsheet = client.open_by_key(
"1pZ9fAhib8oP12GFyhZ6OCUjkTvzcH23o3E8Ap4eR5sU"
)

products_sheet = spreadsheet.worksheet("Products")
sales_sheet = spreadsheet.worksheet("Sales")

#Load Products
products_data = products_sheet.get_all_records()
products_df = pd.DataFrame(products_data)

#Billing Interface
st.title("Electrical Shop Billing")

product = st.selectbox(
"Select Product",
products_df["Product_Name"]
)

row = products_df[products_df["Product_Name"] == product]

price = row["Selling_Price"].values[0]

quantity = st.number_input("Quantity", min_value=1)

payment_type = st.selectbox("Payment Type", ["Cash","Credit"])

total = price * quantity

st.write("Total:", total)

#Save Sale
if st.button("Generate Bill"):

    # find product row index
    product_row_index = products_df[
        products_df["Product_Name"] == product
    ].index[0]

    # get current stock
    current_stock = row["Stock"].values[0]

    # calculate new stock
    new_stock = current_stock - quantity

    # update stock in Products sheet
    products_sheet.update_cell(
        product_row_index + 2,
        3,
        new_stock
    )

    # generate invoice number
    sales_data = sales_sheet.get_all_records()
    invoice_number = f"INV{len(sales_data)+1:03d}"

    # save sale
    sales_sheet.append_row([
        invoice_number,
        pd.Timestamp.now().strftime("%Y-%m-%d"),
        row["Product_ID"].values[0],
        product,
        quantity,
        price,
        total,
        payment_type
    ])

    st.success(f"Bill {invoice_number} created successfully")

















