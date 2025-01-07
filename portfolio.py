import streamlit as st
import mysql.connector

# Page configuration
st.set_page_config(page_title="Vipul Singh Portfolio", page_icon="🧊")

# Styling
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #FFD700 !important; /* Yellow color */
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header and Introduction
st.toast('Welcome to My Portfolio', icon='👋')
col1, col2 = st.columns([1, 1])
col1.title("I am :blue[Vipul Singh]")
col1.header("An Aspiring Analyst")
col2.image(vipulimage.jpg', width=200)

st.subheader("About Me", divider=True)
st.markdown("I am a highly motivated and analytical professional with a Bachelor's of Technology from the Modern Institute of Technology & Research Center, specializing in Artificial Intelligence and Data Science. With a strong foundation in SQL, MySQL Server, Database Admin, Excel, Python, and Power BI, I possess a passion for extracting insights from data. My hands-on experience includes analyzing datasets, developing end-to-end data analysis report dashboards, and creating educational content to simplify complex analytical concepts.")

# Resume Section
st.subheader("Resume", divider=True)
col1, col2 = st.columns([0.4, 1])
with col1:
    st.text("Profile:")
    st.text("Domain:")
    st.text("Education:")
    st.text("Tools:")
    st.text("Other Skills:")
with col2:
    st.text("Data Science & Analytics")
    st.text("Analysis, Dashboards & Trend Forecasting")
    st.text("Bachelor of Engineering")
    st.text("Microsoft Power BI, Excel, MYSQL Server, Git, Jupyter")
    st.text("Vscode, Machine Learning, Python, C")

# Social Links
st.subheader("Connect with me On", divider=True)
col1, col2, col3 = st.columns([0.4, 0.4, 0.4])
col1.link_button("LinkedIn", "https://vipulsingh.com")
col2.link_button("Github", url='https://github.com', icon="🛜")
col3.link_button("Resume", url='https://152')

# Sidebar
st.sidebar.image('vipulimage.jpg', width=250)
st.sidebar.text("Name: Vipul Singh")
st.sidebar.text("Job Role: Aspiring Data Analyst")
st.sidebar.text("Experience: 1 Month")
st.sidebar.text("Address: Rajasthan, India")
st.sidebar.write("Skills")
st.sidebar.progress(80, text="SQL 80%")
st.sidebar.progress(75, text="Python 75%")
st.sidebar.progress(80, text="Data Visualization 80%")
st.sidebar.progress(85, text="Excel & Spreadsheet 85%")
st.sidebar.progress(80, text="Statistical Analysis 75%")

# Tabs Section
tab1, tab2 = st.tabs(["EXCEL", "SQL"])
tab1.header("Below are the projects made using Excel")

# File Download
a = st.button("Rerun")
if a:
    st.rerun()

with open("vipulimage.jpg", "rb") as file:
    st.download_button("Download file", data=file, file_name="vipulimage.jpg", mime="image/jpg")

# Contact Form
st.subheader("How can I Contact You")
with st.form(key='my_form'):
    name = st.text_input("Name", placeholder="ABC DEF")
    email = st.text_input("Email", placeholder="simba@email.com")
    mob_no = st.text_input("Mobile no.", placeholder="80030.....")
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        if name and email and mob_no:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="wc58uyes",
                database="details"
            )
            cursor = mydb.cursor()
            cursor.execute("INSERT INTO INFO (Full_name, Email, Mobile_no) VALUES (%s, %s, %s)", (name, email, mob_no))
            mydb.commit()
            cursor.close()
            st.success("Submitted successfully!")
        else:
            st.error("Please fill in all fields.")
