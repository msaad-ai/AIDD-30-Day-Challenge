import streamlit as st

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero!")
    return num1 / num2

st.title("Simple Calculator")

num1 = st.number_input("Enter first number:", value=0.0, step=0.1)
num2 = st.number_input("Enter second number:", value=0.0, step=0.1)

operation = st.selectbox("Select operation:", ("Add", "Subtract", "Multiply", "Divide"))

result = None
error_message = None

if st.button("Calculate"):
    try:
        if operation == "Add":
            result = add(num1, num2)
        elif operation == "Subtract":
            result = subtract(num1, num2)
        elif operation == "Multiply":
            result = multiply(num1, num2)
        elif operation == "Divide":
            result = divide(num1, num2)
    except ValueError as e:
        error_message = str(e)

if result is not None:
    st.success(f"Result: {result}")
if error_message:
    st.error(error_message)
