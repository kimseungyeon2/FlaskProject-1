from flask import Flask,url_for,render_template,redirect,session,request,Response
from Model import dao
from flask_restful import Resource
import uuid #universally unique identifier
from PIL import Image
from pytesseract import *
from werkzeug.utils import secure_filename
import os
import re
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class Main(Resource):
    def get(self):
        return 'get main'
    def post(self):
        f = request.files['file']
        lang = request.form['lang']
        f.save(os.path.join('Static/public', secure_filename(f.filename)))
        img = Image.open(os.path.abspath('Static/public/'+f.filename))

        result = pytesseract.image_to_string(img)
        
        return result
    def put(self):
        return ''
    def delete(self):
        return ''
