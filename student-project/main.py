import streamlit as st
import pandas as pd
from array_repeater import ArrayRepeater

st.set_page_config(layout="wide")

st.title("The Best Company")

content = """
blah blah blah blah blah blah blah blah blah 
blah blah blah blah blah blah blah blah blah 
blah blah blah blah blah blah blah blah blah 
blah blah blah blah blah blah blah blah blah 
"""
st.info(content)

st.subheader("Our Team")

df = pd.read_csv("data.csv")

col1, _, col2, _, col3 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5])
ar = ArrayRepeater([col1, col2, col3])
for irow, col in zip(df.iterrows(), ar):
    index, row = irow
    firstname = row["first name"]
    lastname = row["last name"]
    role = row["role"]
    image = row["image"]
    with col:
        st.subheader(f"{firstname} {lastname}".title())
        st.write(role)
        st.image(f"images/{image}")

df
