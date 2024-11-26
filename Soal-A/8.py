import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data_file = "students.csv"
df = pd.read_csv(data_file)

# Set the title of the app
st.title("Student Information Dashboard")

# Sidebar option (only Home page)
option = st.sidebar.selectbox(
    "Pilih menu:",
    ["Home"]
)

if option == "Home":
    # Home page content
    st.subheader("Selamat datang di Dashboard Mahasiswa!")
    st.image("students.jpg", caption="Gambar Mahasiswa", use_column_width=True)

    # Display Dataset
    st.subheader("Dataset Mahasiswa")
    st.dataframe(df)

    # Show a bar chart of GPA distribution
    st.subheader("Grafik Distribusi GPA Mahasiswa")

    # Group data by department and calculate average GPA
    gpa_avg = df.groupby("Department")["GPA"].mean().sort_values()

    # Plot the data as a horizontal bar chart
    fig, ax = plt.subplots(figsize=(10, 6))
    gpa_avg.plot(kind='barh', color="skyblue", ax=ax)
    
    # Set labels and title
    ax.set_xlabel("Rata-rata GPA")
    ax.set_ylabel("Jurusan")
    ax.set_title("Rata-rata GPA Berdasarkan Jurusan")

    # Add GPA values to the left of the bars
    for index, value in enumerate(gpa_avg):
        ax.text(value, index, f'{value:.2f}', va='center', ha='left', fontsize=10, color='black')

    # Display the chart
    st.pyplot(fig)
