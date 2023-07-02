import streamlit as st
import subprocess
import openai
import qrcode
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

openai.api_key = "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"
model_name = "gpt-3.5-turbo"

def record_txt(text):
    # テキストファイルに文を追記します
    with open("record.txt", "a") as file:
        file.write(text + "\n")
        
# テキストファイルから項目を読み込む
def read_records(file_path):
    with open(file_path, "r") as file:
        return file.readlines()

def read_file_as_string(file_path):
    with open(file_path, "r") as file:
        file_content = file.read()
    return file_content
   
# 病院のカルテ形式で項目を表示する
def generate_medical_records(records):
    generated_text = ""
    records = records + "の内容をカルテのようにまとめて。"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": records}
        ],
        max_tokens=1000,
        temperature=0.7,
    )
    completion = response.choices[0].message.content.strip()
    generated_text += completion
    return generated_text

def text_to_pdf(input_file, output_file):
    # 1. Register the font
    # pdfmetrics.registerFont(TTFont('IPA Gothic', 'ipag.ttf'))

    # 2. Create a new PDF with Reportlab
    c = canvas.Canvas(output_file)

    # 3. Set the font to the registered font

    # 4. Open the text file
    with open(input_file, 'r', encoding='utf-8') as txt_file:
        lines = txt_file.readlines()

    # 5. Draw the lines to the PDF
    for i, line in enumerate(lines):
        c.drawString(15, 800 - i * 15, line.strip())

    # 6. Save the PDF
    c.save()

st.title('Symptom Checker')

# Essay-type question
basic_address = st.text_area("質問: 住所")
hospital = st.text_area("質問: かかりつけの病院（任意）")
bloodtype = st.text_area("質問: 血液型")
physical_info = st.text_area("質問: 身長(cm), 体重（kg）")
medicine = st.text_area("質問: 内服薬")
allergy = st.text_area("質問: アレルギー")
med_his = st.text_area("質問: 既往歴(箇条書きでも構いません）")
essay_question = st.text_area("質問: 自分で感じる症状を全て記入してください（箇条書きでも構いません）。")
# Integer-type questions
integer_question1 = st.number_input("質問: 年齢を入力してください", value=0, step=1)
# 可能であれば選択ボタンにしたい
gender_question = st.text_area("質問: 性別を入力してください")

basic_disease = st.text_area("質問: 基礎疾患を入力してください")

# Submit button
if st.button("Submit"):
    # Process the form data
    record_txt(basic_address)
    record_txt(hospital)
    record_txt(bloodtype)
    record_txt(physical_info)
    record_txt(medicine)
    record_txt(allergy)
    record_txt(med_his)
    record_txt(essay_question)
    record_txt(basic_disease)
    record_txt(gender_question)
    
    # テキストファイルから項目を読み込んでカルテを生成する
    file_path = "record.txt"  # テキストファイルのパス
    records = read_records(file_path)
    
    file_path = "record.txt"
    file_content = read_file_as_string(file_path)
    
    generated_text = generate_medical_records(file_content)
    
    

    # カルテをファイルに書き込む
    output_file_path = "clinic_record.txt"  # 出力ファイルのパス
    with open(output_file_path, "w") as output_file:
        output_file.write(generated_text)

    text_to_pdf('clinic_record.txt', 'clinic_record.pdf')
    # Move to another file or app using subprocess
    subprocess.Popen(["streamlit", "run", "front_page.py"])
