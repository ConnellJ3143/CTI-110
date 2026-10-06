# Javion Connelly
# 10/6/26
# Determine weekly pay using if/else and streamlit for UI
# Steps to run -> cd into where your file is, to go back is cd..
# python -m streamlit run P3HW2_ConnellyJavion.py

import streamlit as st

st.title("💰Paycheck Calculator💰")

# Get name
name = st.text_input("Enter employee name: ")

# Get hours worked for the week
hours = st.number_input("Enter hours worked for the week: ")

# Get base pay rate
base_payrate = st.number_input("Enter base pay rate: $")


# If statement is true whent they work more than 40 hrs
if hours > 40:
    OT_hours = hours - 40
    OT_pay = OT_hours * (base_payrate*1.5)
    reg_pay = base_payrate * 40
    grosspay = OT_pay + reg_pay
    
if hours <= 40:
    OT_hours = 0
    OT_pay = 0
    reg_pay = base_payrate * hours
    grosspay = OT_pay + reg_pay

# Display results
st.write(f"Employee name: {name}")
st.write(f"Hours Worked: {hours}")
st.write(f"Pay Rate: ${base_payrate:.2f}")
st.write(f"Overtime: {OT_hours}")
st.write(f"Overtime Pay: ${OT_pay:.2f}")
st.write(f"RegHour Pay: ${reg_pay:.2f}")
st.write(f"Gross Pay: ${grosspay:.2f}")