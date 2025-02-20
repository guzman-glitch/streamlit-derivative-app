import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Title
st.title("📈 Calculus Derivative Solver")

# Input function
x = sp.symbols('x')
user_function = st.text_input("Enter a function of x:", "x**2 + 3*x + 5")

try:
    # Convert input to a sympy expression
    function = sp.sympify(user_function)

    # Compute derivatives
    first_derivative = sp.diff(function, x)
    second_derivative = sp.diff(first_derivative, x)

    # Display results
    st.write(f"### Function:  \n📌 **f(x) = {function}**")
    st.write(f"### First Derivative:  \n🔹 **f'(x) = {first_derivative}**")
    st.write(f"### Second Derivative:  \n🔸 **f''(x) = {second_derivative}**")

    # Evaluate derivative at a point
    value = st.number_input("Enter a value of x to evaluate f'(x):", value=0.0)
    result = first_derivative.subs(x, value)
   st.latex(sp.latex(derivative))

    # Plot function and derivative
    def plot_function():
        f_lambdified = sp.lambdify(x, function, "numpy")
        d_lambdified = sp.lambdify(x, first_derivative, "numpy")

        x_vals = np.linspace(-10, 10, 400)
        y_vals = f_lambdified(x_vals)
        dy_vals = d_lambdified(x_vals)

        plt.figure(figsize=(8, 5))
        plt.plot(x_vals, y_vals, label="f(x)", color="blue")
        plt.plot(x_vals, dy_vals, label="f'(x)", color="red", linestyle="dashed")
        plt.axhline(0, color="black", linewidth=0.5)
        plt.axvline(0, color="black", linewidth=0.5)
        plt.title("Function and Its Derivative")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        plt.grid()
        st.pyplot(plt)

    plot_function()

except sp.SympifyError:
    st.error("Invalid function! Please enter a valid mathematical expression.")
