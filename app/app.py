import os
import dataset
import requests
import json
from bs4 import BeautifulSoup
from flask import Flask,jsonify, request, session,  redirect, url_for, render_template, flash,Response
import logging
from logging.handlers import RotatingFileHandler
from flask_cors import  cross_origin
from werkzeug import secure_filename,generate_password_hash, check_password_hash
from flaskext.mysql import MySQL

UPLOAD_FOLDER      = "./static/"
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
mysql = MySQL()

# define the app object as a reservoir for all resources
app = Flask(__name__.split('.')[0])

# get the additional env variables from environment file
app.config.from_json('./.env')

mysql.init_app(app)

@app.route('/')
def default_page():
    """

    for default page loading
    :return: renders the index.html

    """
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp',methods=['POST'])
def signUp():
 
    # read the posted values from the UI
    conn = mysql.connect()
    
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
    _hashed_password = generate_password_hash(_password)
    cursor = conn.cursor()
    cursor.callproc('sp_createUser',(_name,_email,_hashed_password))
    data = cursor.fetchall()
 
    if len(data) is 0:
        conn.commit()
        return render_template('signup.html')
        #return json.dumps({'message':'User created successfully !'})
    else:
        return json.dumps({'error':str(data[0])})

def main():
    logHandler = RotatingFileHandler('info.log', maxBytes=1000, backupCount=1)
    logHandler.setLevel(logging.INFO)
    app.logger.setLevel(logging.INFO)
    app.logger.addHandler(logHandler)
    app.run(host = '127.0.0.1', port = 50000, debug = True)

if __name__ == '__main__':
    main()