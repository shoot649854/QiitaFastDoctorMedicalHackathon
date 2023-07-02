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
    page_bg_img = f'''
    <style>
    @font-face {{
        font-family: 'DejaVuSerif-BoldItalic';
        src: url('fonts/DejaVuSerif-BoldItalic.ttf') format('truetype');
    }}
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
    }}
    .title {{
        text-align: center;
        font-family: 'DejaVuSerif-BoldItalic', serif;
        font-size: 75px;
        margin-top: 70px;
        margin-bottom: 50px;
    }}
    .button-container {{
        display: flex;
        flex-direction: column;
        align-items: center;
    }}
    .button {{
        
        display: block;
        width: 200%;
        font-size: 32px;
        padding: 20px 30px;
        background-color: #4c87bf;
        color: white;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        transition: background-color 0.3s ease;
        margin-bottom: 20px;
    }}
    .button:hover {{
        background-color: #366b9c;
    }}
    .button:active {{
        transform: scale(0.98);
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

path = os.path.dirname(__file__)
set_background(path + '/Medical_background.png')

st.markdown('<h1 class="title">Medi Check</h1>', unsafe_allow_html=True)

# Button container for center alignment
button_container = st.empty()

# Place each button inside the container
with button_container:
    col1, col2, col3 = st.columns(3)

    if col1.button("Medi Check", help="Click here to go to Medi Check page"):
        subprocess.Popen(["streamlit", "run", "MediCheck.py"])

    if col2.button("Medical Record", help="Click here to go to Medical Record page"):
        subprocess.Popen(["streamlit", "run", "MediHistory.py"])

    if col3.button("Voice Record", help="Click here to go to Voice Record page"):
        subprocess.Popen(["streamlit", "run", "VoiceRecord.py"])
