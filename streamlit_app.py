from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

st.title("Welcome to Streamlit!")

checkbox_one = st.checkbox("Yes")
checkbox_two = st.checkbox("No")

if checkbox_one:
    value = "Yes"
elif checkbox_two:
    value = "No"
else:
    value = "No value selected"

st.write(f"You selected: {value}")
