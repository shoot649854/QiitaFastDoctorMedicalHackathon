import streamlit as st
import subprocess

def record_txt(text):
    # テキストファイルに文を追記します
    with open("record.txt", "a") as file:
        file.write(text + "\n")

    

st.title('Symptom Checker')

# Essay-type question
basic_address = st.text_area(" 質問: 住所")
hospital = st.text_area("質問: かかりつけの病院（任意）")
bloodtype = st.text_area("質問: 血液型")
physical_info = st.text_area(" 質問: 身長(cm), 体重（kg）")
medicine = st.text_area("質問: 内服薬")
allergy = st.text_area("質問: アレルギー")
med_his = st.text_area("質問: 既往歴(箇条書きでも構いません）")
essay_question = st.text_area("質問: 自分で感じる症状を全て記入してください（箇条書きでも構いません）。")
# Integer-type questions
integer_question1 = st.number_input("質問: 年齢を入力してください", value=0, step=1)
# 可能であれば選択ボタンにしたい
gender_question = st.text_area("質問: 性別を入力してください")

basic_disease = st.text_area("質問: 基礎疾患を入力してください")



# 住所　担当医（どこの病院の）血液型　身長体重　内服薬　アレルギー　既往歴



# Submit button
if st.button("Submit"):
    # Process the form data
    st.write("Submitted Answers:")
    st.write("Question 1:", essay_question)
    record_txt(essay_question)
    st.write("Question 2:", integer_question1)
    record_txt(str(integer_question1))
    st.write("Question 3:", gender_question)
    record_txt(gender_question)

    # Move to another file or app using subprocess
    subprocess.Popen(["streamlit", "run", "another.py"])
