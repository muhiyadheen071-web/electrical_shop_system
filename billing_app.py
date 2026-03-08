import streamlit as st
import gspread
import pandas as pd
from google.oauth2.service_account import Credentials


# ----------------------------
# GOOGLE SHEETS CONNECTION
# ----------------------------

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


# ----------------------------
# LOAD PRODUCTS
# ----------------------------

products_data = products_sheet.get_all_records()
products_df = pd.DataFrame(products_data)


# ----------------------------
# STREAMLIT UI
# ----------------------------

st.title("Electrical Shop Billing System")

product = st.selectbox(
    "Select Product",
    products_df["Product_Name"]
)

row = products_df[products_df["Product_Name"] == product]

price = row["Selling_Price"].values[0]

stock = row["Stock"].values[0]

st.write(f"Price: {price}")
st.write(f"Stock Available: {stock}")

quantity = st.number_input("Quantity", min_value=1)

payment_type = st.selectbox(
    "Payment Type",
    ["Cash", "Credit"]
)

total = price * quantity

st.subheader(f"Total: {total}")


# ----------------------------
# GENERATE BILL
# ----------------------------

if st.button("Generate Bill"):

    product_row_index = products_df[
        products_df["Product_Name"] == product
    ].index[0]

    current_stock = row["Stock"].values[0]

    # STOCK VALIDATION
    if quantity > current_stock:
        st.error("Not enough stock available")
        st.stop()

    new_stock = current_stock - quantity

    # UPDATE STOCK
    products_sheet.update_cell(
        product_row_index + 2,
        3,
        new_stock
    )

    # GENERATE INVOICE NUMBER
    sales_data = sales_sheet.get_all_records()

    invoice_number = f"INV{len(sales_data)+1:03d}"

    # SAVE SALE
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
