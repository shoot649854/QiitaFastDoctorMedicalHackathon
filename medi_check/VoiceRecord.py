import streamlit as st
import subprocess
from audiorecorder import audiorecorder
import openai
import datetime 
import os
import base64

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

def transcribe_and_save(audio_path):
    openai.api_key = "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"
    GPT_MODEL = "gpt-3.5-turbo"
    
    # オーディオファイルを開く
    audio_file = open(audio_path, "rb")

    # Whisperで音声から文字起こし
    transcript = openai.Audio.transcribe("whisper-1", audio_file)

    # 現在の日付と時刻を取得
    now = datetime.datetime.now()
    
    # 結果をテキストファイルに保存
    with open('transcription.txt', 'w') as f:
        # 日付と時刻を書き込む
        f.write('Date and Time: ' + now.strftime("%Y-%m-%d %H:%M:%S") + '\n\n')
        f.write(transcript.text)

# Add a title to your app
st.title ("大切な情報を録音しよう！")
audio = audiorecorder("録音開始", "録音中")

if len(audio) > 0:

    st.audio(audio.tobytes())

    audio_path = "record.mp3"
    wav_file = open(audio_path, "wb")
    wav_file.write(audio.tobytes())
    wav_file.close()

    transcribe_and_save(audio_path)

if st.button("ホームに戻る"):
    subprocess.Popen(["streamlit", "run", "front_page.py"])

