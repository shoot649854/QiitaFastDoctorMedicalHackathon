import streamlit as st
import subprocess
from audiorecorder import audiorecorder
import openai
import datetime 

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
audio = audiorecorder("ここを押して録音する", "録音中")

if len(audio) > 0:

    st.audio(audio.tobytes())

    audio_path = "record.mp3"
    wav_file = open(audio_path, "wb")
    wav_file.write(audio.tobytes())
    wav_file.close()

    transcribe_and_save(audio_path)
