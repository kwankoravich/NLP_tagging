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
# from sklearn.exceptions import DataConversionWarning
# warnings.filterwarnings(action='ignore', category=DataConversionWarning)

# https://towardsdev.com/build-and-deploy-streamlit-app-dca682aa6acb



#Title
st.title('NLP Tagging')
#sidebar
st.sidebar.header('Choose Prediction model')
st.sidebar.subheader('File Upload')
# uploaded_file = st.file_uploader(label = 'Upload your file, in .txt format', type = ['txt'])

model_choice = st.sidebar.selectbox('Select Prediction Model', ['Sentence Segmentation', 'Name Entity Recognition'], key = '1')

if model_choice == 'Sentence Segmentation':
        uploaded_file = st.file_uploader(label = 'Upload your file, in .txt format', type = ['txt'])
        if uploaded_file is not None:
                file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type}
                st.write(file_details)
                st.success('Text file has been already uploaded, ready for predicion')
                st.info("Press Predict button to show the tagging")
        submit = st.button('Predict')
        if submit:
                # st.ballons()
                ct = CRFTagger()
                # ct = sklearn_crfsuite.CRF()
                ct.set_model_file('model/crf_sentence.tagger')
                
                #Prediction
                preds_list = []
                test_data = uploaded_file
                for sent in test_data:
                        sent_preds = [x[1] for x in ct.tag([s[0] for s in sent])]
                        preds_list.extend(sent_preds)
                
                raw_test_data = [x for x in [s[0] for s in sent]]
                preds_list = list(zip(raw_test_data, preds_list))
                st.text(preds_list[:10])


if model_choice == 'Name Entity Recognition':
        uploaded_file = st.file_uploader(label = 'Upload your file, in .txt format', type = ['txt'])
        if uploaded_file is not None:
                file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type}
                st.write(file_details)
                st.success('Text file has been already uploaded, ready for predicion')
                st.info("Press Predict button to show the tagging")
        submit = st.button('Predict')
        if submit:
                # st.balloons()
                ct = CRFTagger()
                # ct = sklearn_crfsuite.CRF()
                ct.set_model_file('model/crf_ner.tagger')
                
                #Prediction
                preds_list = []
                test_data = uploaded_file
                for sent in test_data:
                        sent_preds = [x[1] for x in ct.tag([s[0] for s in sent])]
                        preds_list.extend(sent_preds)
                
                raw_test_data = [x for x in [s[0] for s in sent]]
                preds_list = list(zip(raw_test_data, preds_list))
                st.text(preds_list[:10])


