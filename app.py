#Import libraries
import os
from flask import Flask, render_template, request

#Import OCR functions
from text_detector import text_detector
from date_detector import data_detector

#Allow files of specific type
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

#Function to check the file extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#Route and function to handle the webpage
@app.route('/')
def home_page():
    return render_template('webpage.html')

#Route and function to handle the upload page
@app.route('/upload', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return render_template('webpage.html', msg='No file selected')
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            return render_template('webpage.html', msg='No file selected')

            # call the OCR function on it
            text = text_detector(file)
            date=date_detector(text)
            
            # extract the text and display it
            return render_template('webpage.html',
                                   msg='Successfully processed',
                                   extracted_text=date)
    elif request.method == 'GET':
        return render_template('webpage.html')

if __name__ == '__main__':
    app.run()
