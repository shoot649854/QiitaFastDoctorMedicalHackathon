import streamlit as st
from PIL import Image
from streamlit.elements.plotly_chart import SHARING_MODES
from PIL import Image, ImageOps
import numpy as np
import base64
import os

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
    
    prediction = model.predict(data)
    return prediction

st.title("Waste Classifier")
uploaded_file = st.file_uploader(" ", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption='Uploaded IMage.', use_column_width=True)
    label = teachable_machine_classification(image, path+'/model.h5')
    battery= (label[0][0])
    biological= (label[0][1])
    brownglass= (label[0][2])
    cardboard= (label[0][3])
    clothes= (label[0][4])
    greenglass= (label[0][5])
    metal= (label[0][6])
    paper= (label[0][7])
    plastic= (label[0][8])
    shoes= (label[0][9])
    trash= (label[0][10])
    whiteglass= (label[0][11])

    if battery >= 0.6:
        st.write("""
                 """)
    elif biological >= 0.6:
        st.write("It's a Biological Waste. It must be disposed")
    elif brownglass >= 0.6:
        st.write("It's a Brown Glass. Brown glass results from materials like carbon, nickel and sulfur being added to molten glass. A brown hue can be used to protect the container’s contents from direct exposure to sunlight and in turn helps preserve the flavor and freshness. Brown glass is mainly used for food and drink preservation.Many curbside recycling programs require you to sort colored glass from the clear glass. However, depending on your municipality, your local recycling facility could have the capacity to accept commingled glass containers. Check with your local recycling program before making a decision to group together or separate. Adding a single unacceptable item to a batch of recyclables can ruin the whole bunch and decrease the recovered glass value. Make sure to always remove metal or plastic lids or neck rings as well. No matter what kind of glass you might be trying to recycle, always check with your recycling facility when in doubt. It is never worth the contamination risk.")
    elif cardboard >= 0.6:
        st.write("It's a Cardboard. As long as your cardboard and paperboard is clean and dry, it should be placed in your recycle bin.  Wet or greasy cardboard like pizza boxes or fast food boxes are considered a contaminate and belong in the garbage.  Wet or contaminated items can jam sorting equipment and ruin good, clean material. To get the most out of your curbside program, be sure to remove any plastic packaging or bags from your boxes.  It’s a good idea to flatten your boxes to make more room in your bin for other recyclables.Recycling cardboard is as simple as it gets.  When you stick to the basics of recycling, the future of curbside recycling programs remains strong for generations to come.")
    elif clothes >= 0.6:
        st.write("It's a Clothes. Clothing recycling is part of textile recycling. It involves recovering old clothing and shoes for sorting and processing. End products include clothing suitable for reuse, cloth scraps or rags as well as fibrous material. Interest in garment recycling is rapidly on the rise due to environmental awareness and landfill pressure. For entrepreneurs, it provides a business opportunity. In addition, various charities also generate revenue through their collection programs for old clothing.")
    elif greenglass >= 0.6:
        st.write("It's a Green Glass. Green glass is very similar to brown glass because it is created by adding ingredients to molten glass, particularly copper, iron and chromium. Green glass protects contents from sun exposure and extreme temperatures, therefore it is mostly used for food and drink safeguarding.Many curbside recycling programs require you to sort colored glass from the clear glass. However, depending on your municipality, your local recycling facility could have the capacity to accept commingled glass containers. Check with your local recycling program before making a decision to group together or separate. Adding a single unacceptable item to a batch of recyclables can ruin the whole bunch and decrease the recovered glass value. Make sure to always remove metal or plastic lids or neck rings as well. No matter what kind of glass you might be trying to recycle, always check with your recycling facility when in doubt. It is never worth the contamination risk.")
    elif metal >= 0.6:
        st.write("It's a Metal. Metals are essential, versatile and can be used in a number of ways. Metals can be used for industrial purposes such as the manufacture of trucks, cars, airplanes, ships, and railways. They can also be used to manufacture domestic items such as cutlery, crockery and even in packaging. The good thing about metal recycling is that metal can be recycled over and over without altering its properties.The most common recyclable metals include aluminum and steel. The other metals, for example, silver, copper, brass and gold, are so valuable that they are rarely thrown away to be collected for recycling. Therefore, they do not create a waste disposal crisis or problem.")
    elif paper >= 0.6:
        st.write("It's a Paper.Paper recycling pertains to the processes of reprocessing waste paper for reuse. Waste papers are either obtained from paper mill paper scraps, discarded paper materials, and waste paper material discarded after consumer use. Examples of the commonly known papers recycled are old newspapers and magazines.Other forms like corrugated, wrapping, and packaging papers among other types of paper are usually checked for recycling suitability before the process. The papers are collected from the waste locations then sent to paper recycling facilities. ")
    elif plastic >= 0.6:
        st.write("It's a Plastic. Plastic can be recycled by taking it to your local plastic recycling stations.Plastic recycling is the reprocessing of plastic waste into new and useful products. When performed correctly, this can reduce dependence on landfill, conserve resources and protect the environment from plastic pollution and greenhouse gas emissions.")
    elif shoes >= 0.6:
        st.write("It's a Shoes. You can take your old or unwanted shoes and boots to most recycling centres, put them in a bring bank or donate them to a charity shop. Where possible they are sold for re-use.")
    elif trash >= 0.6:
        st.write("It's a Trash. It must be disposed")
    elif whiteglass >= 0.6:
        st.write("It's a White Glass. White glass is made from basic glass elements like sand and limestone, and is used for a variety of products like food and beverage containers, electronics, home design items and so much more.")
