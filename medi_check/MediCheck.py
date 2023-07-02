import streamlit as st
import subprocess

def record_txt(text):
    # テキストファイルに文を追記します
    with open("record.txt", "a") as file:
        file.write(text + "\n")

    print("記録が完了しました。")

st.title('Symptom Checker')

# Essay-type question
essay_question = st.text_area("Question 1: 症状を入力してください（箇条書きでも構いません）。:")

# Integer-type questions
integer_question1 = st.number_input("Question 2: 年齢を入力してください", value=0, step=1)
# 可能であれば選択ボタンにしたい
integer_question2 = st.text_area("Question 3: 性別を入力してください")

# Submit button
if st.button("Submit"):
    # Process the form data
    st.write("Submitted Answers:")
    st.write("Question 1:", essay_question)
    record_txt(essay_question)
    st.write("Question 2:", integer_question1)
    st.write("Question 3:", integer_question2)

    # Move to another file or app using subprocess
    subprocess.Popen(["streamlit", "run", "another.py"])
