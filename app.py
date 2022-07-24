import pandas as pd
import numpy as np
import streamlit as st

st.write("""
# Online Substractor

This app substracts two number""")
st.header('User Input Parameters')
def user_input_features():
    a = st.number_input("Enter First Number")
    b = st.number_input("Enter Second Number")
    
    data = {'A': a,
           'B': b
           }
    return data
data = user_input_features()
result = data['A'] - data['B']
st.write(f"\n Result is {result}")
