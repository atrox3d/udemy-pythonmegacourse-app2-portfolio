import streamlit as st

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your enmail address")
    message = st.text_area("Your message")
    button = st.form_submit_button("Submit")
    if button:
        print("Button Pressed")
if button:
    st.info("Submit Button Pressed")