import streamlit as st
import math

# Set up the page
st.set_page_config(page_title="Streamlit Calculator", page_icon="🧮")

st.title("🧮 Streamlit Calculator")

# Sidebar for navigation
option = st.sidebar.selectbox("Select Calculator Type", ["Basic", "Scientific"])

# Function for basic operations
def basic_operations(num1, num2, operation):
    if operation == "Add":
        return num1 + num2
    elif operation == "Subtract":
        return num1 - num2
    elif operation == "Multiply":
        return num1 * num2
    elif operation == "Divide":
        return num1 / num2 if num2 != 0 else "Cannot divide by zero"

# Function for scientific operations
def scientific_operations(num, operation):
    if operation == "Square Root":
        return math.sqrt(num)
    elif operation == "Power":
        return num ** 2
    elif operation == "Log":
        return math.log(num) if num > 0 else "Log undefined for non-positive numbers"

# Basic Calculator
if option == "Basic":
    st.subheader("Basic Calculator")
    num1 = st.number_input("Enter first number", step=1.0)
    num2 = st.number_input("Enter second number", step=1.0)
    operation = st.radio("Select Operation", ["Add", "Subtract", "Multiply", "Divide"])
    
    if st.button("Calculate"):
        result = basic_operations(num1, num2, operation)
        st.success(f"Result: {result}")

# Scientific Calculator
elif option == "Scientific":
    st.subheader("Scientific Calculator")
    num = st.number_input("Enter a number", step=1.0)
    operation = st.radio("Select Operation", ["Square Root", "Power", "Log"])
    
    if st.button("Calculate"):
        result = scientific_operations(num, operation)
        st.success(f"Result: {result}")
