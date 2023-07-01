import streamlit as st
import subprocess
import base64
import os 

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
       data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
        <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
        ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

path = os.path.dirname(__file__)
set_background(path+'/medical_background.png')


# Add a title to your app
st.title("Medi Check")

# Button to go to "Medi Check" page
if st.button("Medi Check", key="medi_check_button", help="Click here to go to Medi Check page"):
    st.markdown("<h2>Medi Check Page</h2>", unsafe_allow_html=True)
    st.write("Welcome to the Medi Check page!")
    subprocess.Popen(["streamlit", "run", "MediCheck.py"])

# Button to go to "Medical Record" page
if st.button("Medical Record", key="medical_record_button", help="Click here to go to Medical Record page"):
    st.markdown("<h2>Medical Record Page</h2>", unsafe_allow_html=True)
    st.write("Welcome to the Medical Record page!")
    subprocess.Popen(["streamlit", "run", "MediHistory.py"])

# Button to go to "Medical Record" page
if st.button("Voice Record", key="Voice_Record_button", help="Click here to go to Voice Record page"):
    st.markdown("<h2>Voice Record Page</h2>", unsafe_allow_html=True)
    st.write("Welcome to the Voice Record page!")
    subprocess.Popen(["streamlit", "run", "VoiceRecord.py"])
