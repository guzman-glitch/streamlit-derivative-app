import sympy as sp
import streamlit as st

# Streamlit App Title
st.markdown("<h1 style='text-align: center; color: blue; font-family: Arial;'>📘 Derivative Calculator</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: gray;'>Created by GUZMAN</h3>", unsafe_allow_html=True)


# Define the variable
x = sp.Symbol('x')

# Get user input function
user_function = st.text_input("Enter a function (use x as variable):", "3*x**4 - 5*x**3 + 2*x - 7")

try:
    # Convert user input into a SymPy expression
    function = sp.sympify(user_function)
    
    # Compute the first derivative
    derivative = sp.diff(function, x)
    
    # Display only the derivative in proper math notation
    st.latex(r"f'(x) = " + sp.latex(derivative))  # ✅ Only shows the derivative

except Exception as e:
    st.error("⚠️ Invalid function! Please enter a valid mathematical expression.")
