import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
from PIL import Image

st.title('Work on progress')

# x = st.slider('x')  # 👈 this is a widget
# st.write(x, 'squared is', x * x)


# uploaded_file = st.file_uploader("Upload Files",type=['png','jpeg'])
# if uploaded_file is not None:
#     file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
#     st.write(file_details) https://blog.jcharistech.com/2020/11/08/working-with-file-uploads-in-streamlit-python/


@st.cache
def load_image(image_file):
	img = Image.open(image_file)
	return img 

image_file = st.file_uploader("Upload Image",type=['png','jpeg','jpg'])
if image_file is not None:

    # To See Details
    # st.write(type(image_file))
    # st.write(dir(image_file))
    file_details = {"Filename":image_file.name,"FileType":image_file.type,"FileSize":image_file.size}
    st.write(file_details)

    img = load_image(image_file)
    st.image(img,width=250,height=250)