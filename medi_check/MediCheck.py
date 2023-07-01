import streamlit as st
import subprocess

st.title('Symptom Checker')

# Essay-type question
essay_question = st.text_area("Question 1: Enter your symptoms:")

# Integer-type questions
integer_question1 = st.number_input("Question 2: Enter an integer", value=0, step=1)
integer_question2 = st.number_input("Question 3: Enter another integer", value=0, step=1)

# Submit button
if st.button("Submit"):
    # Process the form data
    st.write("Submitted Answers:")
    st.write("Question 1:", essay_question)
    st.write("Question 2:", integer_question1)
    st.write("Question 3:", integer_question2)

    # Move to another file or app using subprocess
    subprocess.Popen(["streamlit", "run", "another.py"])
