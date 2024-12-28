import streamlit as st

# Set page title and layout
st.set_page_config(page_title="Simple Calculator", layout="centered")

# App title
st.title("🧮 Simple Calculator")

# Input fields
num1 = st.number_input("Enter the first number:", value=0.0, step=0.1, format="%.2f")
num2 = st.number_input("Enter the second number:", value=0.0, step=0.1, format="%.2f")

# Operation selection
operation = st.selectbox(
    "Select an operation:",
    ("Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)"),
)

# Perform calculation
if st.button("Calculate"):
    if operation == "Addition (+)":
        result = num1 + num2
        st.success(f"The result of {num1} + {num2} is: {result}")
    elif operation == "Subtraction (-)":
        result = num1 - num2
        st.success(f"The result of {num1} - {num2} is: {result}")
    elif operation == "Multiplication (*)":
        result = num1 * num2
        st.success(f"The result of {num1} × {num2} is: {result}")
    elif operation == "Division (/)":
        if num2 != 0:
            result = num1 / num2
            st.success(f"The result of {num1} ÷ {num2} is: {result}")
        else:
            st.error("Error: Division by zero is not allowed!")
