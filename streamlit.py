import warnings
warnings.filterwarnings("ignore")
import streamlit as st


# Function to find the largest number
def find_largest(a, b, c):
    return max(a, b, c)

# Streamlit UI
st.title("Find the Largest Among Three Numbers")

a = int(st.number_input("Enter the first number:", value=0, step=1))
b = int(st.number_input("Enter the second number:", value=0, step=1))
c = int(st.number_input("Enter the third number:", value=0, step=1))

# Find largest number
if st.button("Find the Largest"):
    largest = find_largest(a, b, c)
    st.success(f"The largest number is {largest}")



