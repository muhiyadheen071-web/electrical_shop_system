import streamlit as st

st.title("Electrical Shop Billing System")

product = st.text_input("Product Name")

quantity = st.number_input("Quantity", min_value=1)

price = st.number_input("Price", min_value=0.0)

payment_type = st.selectbox(
    "Payment Type",
    ["Cash", "Credit"]
)

if st.button("Generate Bill"):
    total = quantity * price
    st.success(f"Total Bill: {total}")
