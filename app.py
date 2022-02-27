from flask import Flask, redirect, url_for, render_template, request
from werkzeug.utils import secure_filename
import flask
import pycrfsuite
import os
# import sklearn_crfsuite
from nltk.tag import CRFTagger
from logging import FileHandler,WARNING

with open(f'model/crf_ner.tagger', 'rb') as m:
    ct = CRFTagger()
    # ct = sklearn_crfsuite.CRF()
    ct.set_model_file('/home/superai2-279/webapp/model/crf_ner.tagger')

# with open(f'model/crf_sentence.tagger', 'rb') as m:
#     ct = CRFTagger()
#     # ct = sklearn_crfsuite.CRF()
#     ct.set_model_file('/home/superai2-279/webapp/model/crf_sentence.tagger')

app = Flask(__name__, template_folder='templates')
file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)
# @app.route('/')
# def main():
#     return(flask.render_template('main.html'))
app.config["UPLOAD_FOLDER"] = "static/"

@app.route('/')
def show_image():
    filename = os.path.join(app.config['UPLOAD_FOLDER'], 'Data_example.jpg')
    return render_template("index.html", data_template = filename)

@app.route('/')
def upload_file():
    return render_template('index.html')


@app.route('/', methods=['GET'])
def dropdown():
        tasks = ['Sentence Segmentation', 'Name Entity Recognition']
        return render_template('index.html', tasks = tasks)


# @app.route('/display', methods = ['GET', 'POST'])
# def save_file():
#     if request.method == 'POST':
#         f = request.files['file']
#         filename = secure_filename(f.filename)
#         f.save(app.config['UPLOAD_FOLDER'] + filename)

#         file = open(app.config['UPLOAD_FOLDER'] + filename,"r")
#         content = file.read()
        
        
#     return render_template('content.html', content=content)

def read_file_test(path_file):

    test_data, test_crf = [], []
    with open(path_file, 'r', encoding = 'utf-8') as f:
        for output in f:
            output = output.split('\n')
            output = output[0]
            #print(output)
            if output != '':
              test_data.append((output, ''))
            else:
              test_data.append(('', 'O'))
              test_crf.append(test_data)
              test_data = []
    return test_crf



@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))
    if flask.request.method == 'POST':
        # sentence = flask.request.form['sentence']
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(app.config['UPLOAD_FOLDER'] + filename)

        file = open(app.config['UPLOAD_FOLDER'] + filename,"r")
        # content = file.read()
        test_data = read_file_test(app.config['UPLOAD_FOLDER'] + filename)
        
        preds_list = []
        for sent in test_data:
            sent_preds = [x[1] for x in ct.tag([s[0] for s in sent])]
            preds_list.extend(sent_preds)
        
        raw_test_data = [x for x in [s[0] for s in sent]]
        preds_list = list(zip(raw_test_data, preds_list))
        # prediction = ct.tag([sentence])
        # return flask.render_template('main.html',
        #                              original_input={'Sentence':sentence},
        #                              result=prediction,
        #                              )
        return flask.render_template('main.html',
                                     original_input={'File':filename},
                                     result=preds_list[0:10],
                                     )



if __name__ == '__main__':
    app.run()