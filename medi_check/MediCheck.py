import streamlit as st
import subprocess
import openai

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
    
# 病院のカルテ形式で項目を表示する
def generate_medical_records(records):
    generated_text = ""
    for record in records:
        prompt = f"Patient: {record}"
        response = openai.ChatCompletion.create(
            model=model_name,
            messages=[
                {"role": "system", "content": "You are a doctor."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=50,  # 応答の最大トークン数
            temperature=0.7,  # 生成の多様性を調整
        )
        completion = response.choices[0].message.content.strip()
        generated_text += f"AI: {completion}\n"
    return generated_text

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
    record_txt("腹痛、熱")
    record_txt("20")
    record_txt("男")
    record_txt("青森県十和田市")
    record_txt("なし")
    record_txt("O")
    record_txt("160cm 50kg")
    record_txt("なし")
    record_txt("なし")
    record_txt("おたふく")
    
    # テキストファイルから項目を読み込んでカルテを生成する
    file_path = "record.txt"  # テキストファイルのパス
    records = read_records(file_path)
    generated_text = generate_medical_records(records)

    # カルテをファイルに書き込む
    output_file_path = "clinic_record.txt"  # 出力ファイルのパス
    with open(output_file_path, "w") as output_file:
        output_file.write(generated_text)
    
    # Move to another file or app using subprocess
    subprocess.Popen(["streamlit", "run", "front_page.py"])
