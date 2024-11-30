import streamlit as st

# Title for the calculator
st.title("Simple Calculator")

# Input fields for the two numbers
number1 = st.number_input("Enter the first number:", value=0.0, step=1.0)
number2 = st.number_input("Enter the second number:", value=0.0, step=1.0)

# Dropdown for selecting an operation
operation = st.selectbox("Select an operation:", ["Addition", "Subtraction", "Multiplication", "Division"])

# Calculate button
if st.button("Calculate"):
    try:
        if operation == "Addition":
            result = number1 + number2
        elif operation == "Subtraction":
            result = number1 - number2
        elif operation == "Multiplication":
            result = number1 * number2
        elif operation == "Division":
            if number2 != 0:
                result = number1 / number2
            else:
                st.error("Division by zero is not allowed!")
                result = None
        
        if result is not None:
            st.success(f"The result of {operation} is: {result}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
