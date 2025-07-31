import streamlit as st
from datetime import date

st.set_page_config(page_title="Age Calculator", page_icon="🎂")

st.title("🎂 Age Calculator")
st.subheader("Enter your Date of Birth:")

# 🎯 Date of Birth Input
dob = st.date_input("Date of Birth", min_value=date(1900, 1, 1))

# 🎯 Today's Date
today = date.today()

# 🎯 Calculate Age
if dob:
    age_years = today.year - dob.year
    if (today.month, today.day) < (dob.month, dob.day):
        age_years -= 1

    st.success(f"🎉 Your age is : {age_years} years")

