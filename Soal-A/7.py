import streamlit as st
import pandas as pd
import numpy as np

# Membuat DataFrame dengan nilai acak
df = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['x', 'y']
)

# Line Chart
st.title("Line Chart")
st.line_chart(df)

# Bar Chart
st.title("Bar Chart")
st.bar_chart(df)

# Area Chart
st.title("Area Chart")
st.area_chart(df)
