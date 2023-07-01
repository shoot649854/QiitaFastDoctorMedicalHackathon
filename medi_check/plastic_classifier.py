import streamlit as st
from audiorecorder import audiorecorder

st.title('Symptom Checker')

# Add search bar for symptom input
symptoms = st.text_input('Enter your symptoms:')

if st.button('Search'):
    # Perform search based on symptoms
    # Replace this with your actual search logic
    search_results = perform_search(symptoms)
    
    # Display search results
    for result in search_results:
        st.write(result)

st.title ("大切な情報を録音しよう！")
audio = audiorecorder("ここを押して録音する", "録音中")

if len(audio) > 0:

    st.audio(audio.tobytes())

    wav_file = open("audio.mp3", "wb")
    wav_file.write(audio.tobytes())