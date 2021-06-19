import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


import joblib

#loading random forest model
#rf_model = joblib.load(open('/home/arun/Documents/mlwebapp/models/rf.pkl', 'rb'))

st.title('MNIST Digit Recognizer')

rf_model = joblib.load(open('/home/arun/Documents/mlwebapp/models/rf.pkl', 'rb'))
def load_rf_model():
    rf_model = joblib.load(open('/home/arun/Documents/mlwebapp/models/rf.pkl', 'rb'))
    return rf_model





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

### load image and view image
image_file = st.file_uploader("Upload Image",type=['png','jpeg','jpg'],accept_multiple_files=True,)

@st.cache
def load_image(image_file):
	img = Image.open(image_file)
	return img



def imgshow(image_file):
    #option = show_options()
    for i in image_file:
        #print(type(i))
        
        if i is not None:    
            img = load_image(i)
            st.image(img,width=250,height=250)
            file_details = {"Filename":i.name,"FileType":i.type,"FileSize":i.size}

            #show options and run predictions based on selected options
            #option = show_options()
            # if option == 'RF':
            #     print('RL selected')
            #     pred(img,rf_model)
            # else:
            #     pass
            # pred(img,rf_model)

        else:
            pass
    option = show_options()
    if option == 'RF':
        print('RL selected')
        for i in image_file:
            img = load_image(i)
            pred(img,rf_model)
    else:
        pass
       
    return 
#############


def show_options():
    option = st.selectbox(
        'Select the model you need to run predictions on (only RF model availble)',
        ('SVM', 'RF','Deep CNN'))
    #print(option)

    st.write('Selected  :', option)
    return option



imgshow(image_file)
