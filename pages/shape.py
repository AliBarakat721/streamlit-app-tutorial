import streamlit as st
import math
import time

# Page configuration
st.set_page_config(page_title="Shapes Calculator", page_icon="📐", layout="wide")
st.title("Shapes Calculator")
st.markdown("This application calculates the area and perimeter of various geometric shapes.")

# Sidebar configuration for settings
st.sidebar.header("Configuration")
shape = st.sidebar.selectbox("Choose Shape:", ['Circle', 'Rectangle', 'Triangle', 'Square'])

# Section for Circle calculation
if shape == 'Circle':
    st.subheader("Circle")
    radius = st.number_input("Enter the radius:", min_value=0.0, max_value=10000.0, step=0.1)
    if st.button("Calculate", key="circle_calc"):
        with st.spinner("Calculating..."):
            time.sleep(1)
            area = math.pi * radius ** 2
            perimeter = 2 * math.pi * radius
            st.success("Results:")
            st.write("Area:", area)
            st.write("Perimeter:", perimeter)

# Section for Rectangle calculation
elif shape == 'Rectangle':
    st.subheader("Rectangle")
    col1, col2 = st.columns(2)
    with col1:
        width = st.number_input("Width:", min_value=0.0, max_value=1000.0, step=0.1)
    with col2:
        height = st.number_input("Height:", min_value=0.0, max_value=1000.0, step=0.1)
    if st.button("Calculate", key="rect_calc"):
        with st.spinner("Calculating..."):
            time.sleep(1)
            area = width * height
            perimeter = 2 * (width + height)
            st.success("Results:")
            st.write("Area:", area)
            st.write("Perimeter:", perimeter)

# Section for Triangle calculation using Heron's formula
elif shape == 'Triangle':
    st.subheader("Triangle")
    col1, col2, col3 = st.columns(3)
    with col1:
        a = st.number_input("Side A:", min_value=0.0, max_value=1000.0, step=0.1)
    with col2:
        b = st.number_input("Side B:", min_value=0.0, max_value=1000.0, step=0.1)
    with col3:
        c = st.number_input("Side C:", min_value=0.0, max_value=1000.0, step=0.1)
    if st.button("Calculate", key="tri_calc"):
        with st.spinner("Calculating..."):
            time.sleep(1)
            # Check if the sides form a valid triangle using the triangle inequality
            if a + b > c and a + c > b and b + c > a:
                s = (a + b + c) / 2
                area = math.sqrt(s * (s - a) * (s - b) * (s - c))
                perimeter = a + b + c
                st.success("Results:")
                st.write("Area:", area)
                st.write("Perimeter:", perimeter)
            else:
                st.error("The entered sides do not form a valid triangle.")

# Section for Square calculation
elif shape == 'Square':
    st.subheader("Square")
    side = st.number_input("Enter the side length:", min_value=0.0, max_value=1000.0, step=0.1)
    if st.button("Calculate", key="sq_calc"):
        with st.spinner("Calculating..."):
            time.sleep(1)
            area = side * side
            perimeter = 4 * side
            st.success("Results:")
            st.write("Area:", area)
            st.write("Perimeter:", perimeter)

# Additional sidebar section for extra information
st.sidebar.markdown("---")
st.sidebar.info("Application developed by [Ali Barakat]. Enjoy using the Shapes Calculator!")
