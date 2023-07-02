import streamlit as st
from audiorecorder import audiorecorder
import os
import base64

path = os.path.dirname(__file__)

st.title(' ')
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
       data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
        <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
        ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background(path+'/background.png')


def teachable_machine_classification(img, file):
    np.set_printoptions(suppress=True)
    model = keras.models.load_model(file)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = img
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    st.write("Start Predection...")
    data[0] = normalized_image_array
    
    # Display search results
    for result in search_results:
        st.write(result)

st.title ("大切な情報を録音しよう！")
audio = audiorecorder("ここを押して録音する", "録音中")

if len(audio) > 0:

    st.audio(audio.tobytes())

    wav_file = open("audio.mp3", "wb")
    wav_file.write(audio.tobytes())