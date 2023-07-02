import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import datetime

def soap_format():
    # テキストファイルから情報を読み取る
    with open('transcription.txt', 'r') as f:
        lines = f.readlines()
        
    # テキストファイルの情報をSOAPフォーマットに整理
    date_time, text = lines[0], lines[2:]
    s, o, a, p = '', '', '', ''
    for line in text:
        if 'subjective' in line.lower():
            s = line
        elif 'objective' in line.lower():
            o = line
        elif 'assessment' in line.lower():
            a = line
        elif 'plan' in line.lower():
            p = line
    return date_time, s, o, a, p

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

def main():
    date_time, s, o, a, p = soap_format()
    create_pdf(date_time, s, o, a, p)

    # Add a download button for the PDF
    with open("soap.pdf", "rb") as f:
        btn = st.download_button(
            "Download SOAP PDF",
            f,
            file_name='soap.pdf',
            mime='application/pdf'
        )

main()