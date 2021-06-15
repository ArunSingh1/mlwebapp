import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
from PIL import Image


import joblib

#loading random forest model
def load_models():
    rf_model = joblib.load(open('rf.pkl', 'rb'))
    return rf_model

st.title('MNIST Digit Recognizer')

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

def pred(img,model):

    seq = img.getdata()
    image_array = np.array(seq)
    #print(image_array.shape)
    topred = np.array(image_array)[np.newaxis, :] 
    #print(topred.shape)
    pred = model.predict(topred)

    print("prediction ",  str(pred[0]))

    #st.write(dir(model))
    prediction  =  "Predicted label - {}".format(model) + " = " + str(pred[0]) 
    st.text(prediction)
    return prediction


image_file = st.file_uploader("Upload Image",type=['png','jpeg','jpg'])
if image_file is not None:
    
    img = load_image(image_file)
    st.image(img,width=250,height=250)

    pred(img,rf_model)
    # pred(img,knn_model)
    # To See Details
    # st.write(type(image_file))
    # st.write(dir(image_file))
    file_details = {"Filename":image_file.name,"FileType":image_file.type,"FileSize":image_file.size}
    #st.write(file_details)

    #st.text(predd)


	
option = st.selectbox(
'Select the model you need to run predictions on',
('RF', 'SVM', 'Deep CNN'))

print(option)

st.write('You selected:', option)

def call_pred(img,model,option):
    rf_model = load_models()
    seq = img.getdata()
    image_array = np.array(seq)
    #print(image_array.shape)
    topred = np.array(image_array)[np.newaxis, :] 

    if option == 'RF':
        pred(img,rf_model)
    
    elif option == 'SVM':
        pred(img,rf_model)




