from flask import Flask, render_template, redirect, request, session, flash

import re
# the "re" module will let us perform some regular expression operations
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

Name_REGEX = re.compile(r'^[a-zA-Z]+$')

app= Flask(__name__)

app.secret_key="thisisasecret"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success', methods=['POST'])
def suc():
    session ['email'] = request.form ['email']
    session ['first_name'] = request.form ['first_name']
    session ['last_name'] = request.form ['last_name']
    session ['email'] = request.form ['email']
    session ['password'] = request.form ['password']
    session ['password_confirm'] = request.form ['password_confirm']

    if len (request.form['first_name']) <1:
        flash('All fields are required and must not be blank')
    elif len (request.form['last_name']) <1:
        flash('All fields are required and must not be blank')
    elif len(request.form['email']) <1:
        flash('All fields are required and must not be blank')
    elif len (request.form['password']) <1:
        flash('All fields are required and must not be blank')
    elif len (request.form['password_confirm']) <1:
        flash('All fields are required and must not be blank')


    elif not Name_REGEX.match(request.form['first_name']):
        flash ('First name cannot contain any numbers')
    elif not Name_REGEX.match(request.form['last_name']):
        flash ('Last name cannot contain any numbers')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash ('Email should be a valid email')
    elif len(request.form['password']) < 8:
        flash ('Password should be more than 8 characters')
    elif len (request.form['password_confirm']) < 8:
        flash ('Password should be more than 8 characters')
    elif request.form['password'] != request.form['password_confirm']:
        flash('Password and Password Confirmation should match')
    else:
        flash('Thanks for submitting your information. You are now registered!!!')
    return redirect ('/')
app.run(debug=True)
