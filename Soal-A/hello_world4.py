import streamlit as st

# Form Header
st.title("Interactive Form")

# Checkbox
agree = st.checkbox("yes")

# Button
if st.button("Click"):
    st.write("Button clicked!")

# Radio Button for Gender
gender = st.radio("Pick your gender", ("Male", "Female"))

# Dropdown for Gender (redundant in this case)
dropdown_gender = st.selectbox("Pick your gender", ["Male", "Female"])

# Dropdown for Planet
planet = st.selectbox("choose a planet", ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"])

# Slider for Marks
mark = st.slider("Pick a mark", 0, 100, 50)
if mark > 75:
    st.write(f"Selected mark: Exellent")
elif mark > 50:
    st.write(f"Selected mark: Good")
else:
    st.write(f"Selected mark: Bad")

# Slider for Number
number = st.slider("Pick a number", 0, 50, 9)
st.write(f"Selected number: {number}")
