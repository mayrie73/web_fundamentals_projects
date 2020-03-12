from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
mysql = MySQLConnector(app,'emaildb')
app.secret_key = "ThisIsSecret!"
@app.route('/')
def index():
    query = "SELECT * FROM emails"                           
    emails = mysql.query_db(query) 
    return render_template("index.html")
@app.route('/process', methods=['POST'])
def create():
    query = "INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
    data = {
             'email': request.form['email'],
           }
    mysql.query_db(query, data)
    return redirect('/')   
@app.route('/process', methods=['POST'])
def submit():
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    else:
        flash("Success!")
        mysql.query_db(query, data)
        return redirect('/success')
    return redirect('/')
@app.route('/success')
def success():
    query = "SELECT email, created_at FROM emails"
    emails = mysql.query_db(query)
    return render_template("success.html", emails = emails)
app.run(debug=True)
