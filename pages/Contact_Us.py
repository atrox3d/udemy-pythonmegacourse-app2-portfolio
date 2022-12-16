import streamlit as st
import mailer
st.header("Contact Me")

with st.form(key="email_form", clear_on_submit=True):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message")
    button = st.form_submit_button("Submit")
    if button:
        if user_email and message:
            subject = f"Message form from {user_email}"
            st.info("Sending email...")
            mailer.send_mail(subject, message)
            st.info("Email sent succesfully")
        else:
            st.error("Please provide email and message")
