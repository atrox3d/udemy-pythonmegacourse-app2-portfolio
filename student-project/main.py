import streamlit as st
import pandas as pd

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
cols = [col1, col2, col3]
colidx = 0
for index, row in df.iterrows():
    firstname = row["first name"]
    lastname = row["last name"]
    role = row["role"]
    image = row["image"]
    with cols[colidx]:
        st.subheader(f"{firstname} {lastname}".title())
        st.write(role)
        st.image(f"images/{image}")
    colidx = (colidx + 1) % 3

df
