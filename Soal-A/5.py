import streamlit as st

# Form Header
st.title("Interactive Form")

# Input Number
number = st.number_input("Pick a number", min_value=1, max_value=100, value=1, step=1)

# Input Email
email = st.text_input("Email address")

# Input Date
travel_date = st.date_input("Travelling date")

# Input Time
school_time = st.time_input("School time")

# Input Multiline Text (Description)
description = st.text_area("Description")

# File Uploader
uploaded_file = st.file_uploader("Upload a photo", type=["png", "jpg", "jpeg"])

# Color Picker
favorite_color = st.color_picker("Choose your favourite color", "#ff00ff")

# Submit Button
if st.button("Submit"):
    st.success("Form submitted successfully!")
    st.write("### Form Data:")
    st.write(f"Number: {number}")
    st.write(f"Email: {email}")
    st.write(f"Travel Date: {travel_date}")
    st.write(f"School Time: {school_time}")
    st.write(f"Description: {description}")
    if uploaded_file:
        st.write(f"Uploaded File: {uploaded_file.name}")
    st.write(f"Favorite Color: {favorite_color}")
