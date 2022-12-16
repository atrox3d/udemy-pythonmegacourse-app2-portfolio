import streamlit as st
import pandas as pd
import mailer

topics = pd.read_csv('topics.csv')

with st.form(key="contact-form", clear_on_submit=True):
    user_email = st.text_input("Your Email Address")
    topic = st.selectbox("What topic do you want to discuss?", topics.topic)
    message = st.text_area("Message Text")
    button = st.form_submit_button()
    if button:
        if user_email and topic and message:
            subject = f"{topic} request from {user_email}"
            st.info("Sending email...")
            mailer.send_mail(subject, message)
            st.info("Email sent successfully!")
        else:
            st.error("Please fill all the fields")
