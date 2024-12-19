import streamlit as st 
import pandas as pd
import numpy as np

# Title
st.title("Hello this is my first program on streamlit")

# Display simple text
st.write("This is simple text")

# Create a simple data frame
# A DataFrame is a two-dimensional, tabular data structure used primarily in Python's pandas library. It is one of the most commonly used data structures in data analysis and manipulation because it provides a convenient way to work with structured data.
db = pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]
})
# display the data frame
st.write("this is my data frame")
st.write(db)

# Create a line chart
chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=["a","b","c"]
)
st.line_chart(chart_data)