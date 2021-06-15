import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import joblib
import requests

#loading random forest model
#rf_model = joblib.load(open('/home/arun/Documents/mlwebapp/models/rf.pkl', 'rb'))

st.title('MNIST Digit Recognizer')

base_url = 'http://127.0.0.1:8000'


rf_model = joblib.load(open('/home/arun/Documents/mlwebapp/models/rf.pkl', 'rb'))
def load_rf_model():
    rf_model = joblib.load(open('/home/arun/Documents/mlwebapp/models/rf.pkl', 'rb'))
    return rf_model


def to_img_array(img):
    seq = img.getdata()
    image_array = np.array(seq)
    #print(image_array.shape)
    topred = np.array(image_array)[np.newaxis, :] 
    return topred

### load image and view image
image_file = st.file_uploader("Upload Image",type=['png','jpeg','jpg'])

@st.cache
def load_image(image_file):
	img = Image.open(image_file)
	return img

import json
#test_url = 'http://127.0.0.1:8000/testing/imgdata/DEEPCNN'
def imgshow(image_file):
    if image_file is not None:    
        img = load_image(image_file)
        st.image(img,width=250,height=250)
        file_details = {"Filename":image_file.name,"FileType":image_file.type,"FileSize":image_file.size}

        #preprocess image into array
        topred = to_img_array(img)
        
        #changed to json for api post
        topred2 = json.dumps(topred.tolist())

        print(type(topred))

        #show options and run predictions based on selected options
        option = show_options()
        if option == 'RF':
            print('RL selected')
            test_url = 'http://127.0.0.1:8000/testing/{}/RF'.format(topred2)
            resp = requests.get(test_url)
            to = resp.json()
            print(to)
            st.text(to)

        elif option == 'Deep CNN':
            test_url = 'http://127.0.0.1:8000/testing/{}/DEEPCNN'.format(topred2)
            resp = requests.get(test_url)
            to = resp.json()
            print(to)
            st.text(to)
            
        else:
            test_url = 'http://127.0.0.1:8000/testing/{}/SVM'.format(topred2)
            resp = requests.get(test_url)
            to = resp.json()
            print(to)
            st.text(to)

    else:
        pass
    return 
#############


def show_options():
    option = st.selectbox(
        'Select the model you want to run predictions on',
        ('SVM', 'RF','Deep CNN'))
    #print(option)

    st.write('Selected Model:', option)
    return option


imgshow(image_file)




# def pred(img,model):

#     seq = img.getdata()
#     image_array = np.array(seq)
#     #print(image_array.shape)
#     topred = np.array(image_array)[np.newaxis, :] 
#     #print(topred.shape)
#     pred = model.predict(topred)

#     print("prediction ",  str(pred[0]))

#     #st.write(dir(model))
#     prediction  =  "Predicted label - {}".format(model) + " = " + str(pred[0]) 
#     st.text(prediction)
#     return prediction