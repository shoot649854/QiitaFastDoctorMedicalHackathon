import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import datetime
import os
import base64
import subprocess

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

def soap_format(dataframe):
    today = date.today()
    return str(today.strftime("%b-%d-%Y")), str(dataframe['subjective'].iloc[0]), str(dataframe['objective'].iloc[0]), str(dataframe['assessment'].iloc[0]), str(dataframe['Plan'].iloc[0])

# def soap_format():
#     # テキストファイルから情報を読み取る
#     with open('transcription.txt', 'r') as f:
#         lines = f.readlines()
        
#     # テキストファイルの情報をSOAPフォーマットに整理
#     date_time, text = lines[0], lines[2:]
#     s, o, a, p = '', '', '', ''
#     for line in text:
#         if 'subjective' in line.lower():
#             s = line
#         elif 'objective' in line.lower():
#             o = line
#         elif 'assessment' in line.lower():
#             a = line
#         elif 'plan' in line.lower():
#             p = line
#     return date_time, s, o, a, p

def create_pdf(date_time, s, o, a, p):
    c = canvas.Canvas("soap.pdf", pagesize=letter)
    width, height = letter
    c.setFont("Helvetica", 12)
    
    y = height - 50  # start from top of page

    # Add date and time
    c.drawString(50, y, date_time)
    y -= 50
    
    # Add SOAP information
    for label, text in [('Subjective:', s), ('Objective:', o), ('Assessment:', a), ('Plan:', p)]:
        if text == '':
            text = 'No information provided.'
        c.drawString(50, y, label)
        y -= 20
        c.drawString(50, y, text)
        y -= 50

    c.save()

# def create_pdf(dataframe):
#     c = canvas.Canvas("soap.pdf", pagesize=letter)
#     width, height = letter
#     c.setFont("Helvetica", 12)

#     y = height - 50  # start from top of page

#     # Add date and time
#     today = date.today()
#     c.drawString(50, y, today.strftime("%b-%d-%Y"))
#     y -= 50
#     c.drawString(50, y, st.table(dataframe.head()))




def main():
    st.write("You Login as Patient-1")
    dataframe = pd.read_csv('../SOAP/2023-category.csv')
    st.table(dataframe.head())
    # date_time, s, o, a, p = soap_format(dataframe)
    date_time, s, o, a, p = soap_format(dataframe)
    create_pdf(date_time, s, o, a, p)
    st.title("SOAP Download")

    import pandas as pd
    dataframe = pd.read_csv('../SOAP/2023-category.csv')
    st.table(dataframe)
    # Add a download button for the PDF
    with open("soap.pdf", "rb") as f:
        btn = st.download_button(
            "Download SOAP PDF",
            f,
            file_name = 'soap.pdf',
            mime = 'application/pdf'
        )
main()

if st.button("ホームに戻る"):
    subprocess.Popen(["streamlit", "run", "front_page.py"])
