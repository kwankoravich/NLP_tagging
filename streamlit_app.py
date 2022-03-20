from distutils.command.upload import upload
from app import upload_file
import pycrfsuite
import os
# import sklearn_crfsuite
from nltk.tag import CRFTagger

import streamlit as st
import pandas as pd
# from func import FeatureSelector
# from charts import *
# from models import ModelRunner
import warnings
from sklearn.exceptions import DataConversionWarning
warnings.filterwarnings(action='ignore', category=DataConversionWarning)

# https://towardsdev.com/build-and-deploy-streamlit-app-dca682aa6acb



#Title
st.title('NLP Tagging')
#sidebar
st.sidebar.header('Choose Prediction model')
st.sidebar.subheader('File Upload')
# uploaded_file = st.file_uploader(label = 'Upload your file, in .txt format', type = ['txt'])

model_choice = st.sidebar.selectbox('Select Prediction Model', ['Sentence Segmentation', 'Name Entity Recignition'], key = '1')

if model_choice == 'Sentence Segmentation':
        uploaded_file = st.file_uploader(label = 'Upload your file, in .txt format', type = ['txt'])
        if uploaded_file is not None:
                file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type}
                st.write(file_details)


