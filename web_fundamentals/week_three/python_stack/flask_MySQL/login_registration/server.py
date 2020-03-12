from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
import re
import os, binascii # include this at the top of your file
salt = binascii.b2a_hex(os.urandom(15))

app = Flask(__name__)

mysql = MySQLConnector(app, 'login_registration')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app.secret_key = 'thisisasecret'

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

# route that handles login or register requests
@app.route('/register', methods=['POST'])
def create():
    errors = []
    query = 'SELECT * FROM users WHERE email = :email'
    email = request.form['email']
    data = {'email' : email}
    try:
        user = mysql.query_db(query, data)
        if user: # this will return a value if the email is already in the db
            flash('This email has already been registered!')
            return redirect('/')
    except:
        none = False
        # This was entered because there needed to be an 'except' 

        # checks that first_name is only letters and is at least 2 characters
    if not request.form['first_name'].isalpha():
        errors.append('First name must contain only letters')
    elif len(request.form['first_name']) < 2:
        errors.append('First name must be at least 2 characters long')

        # checks that last_name is only letters and is at least 2 characters
    if not request.form['last_name'].isalpha():
        errors.append('Last name must contain only letters')
    elif len(request.form['last_name']) < 2: 
        errors.append('Last name must be at least 2 characters long')
     
        # checks that email is valid
    if not EMAIL_REGEX.match(request.form['email']):
        errors.append('Email is not valid')

        # checks that password is more than 8 characters and compares the two passwords
    if len(request.form['password']) < 8:
        errors.append('Password must contain at least 8 characters')
    elif not request.form['password'] == request.form['re_password']:
        errors.append('The passwords do not match')

        # if errors are found they are flashed and the rerouted to '/'
        # if no errors the password is hashed and user data stored in the db
    if errors:
        for error in errors:
            flash(error)
        return redirect('/')
    else:
        hashed_pw = bcrypt.generate_password_hash(request.form['password'])
        data ={
            'first_name' : request.form['first_name'],
            'last_name' : request.form['last_name'],
            'email' : request.form['email'],
            'password' : hashed_pw
        }
        query = "INSERT INTO users(first_name, last_name, email, password, created_at, \
        updated_at) VALUES(:first_name, :last_name, :email, :password, NOW(), NOW())"

        # stores user data in the db and sets session to the correct id
        new_user_id = mysql.query_db(query, data)
        if new_user_id is not 0:
            session['id'] = new_user_id
        else:
            flash('Unknown error occured')
        return redirect('/success')

        # route for a successful login/register
@app.route('/success', methods=['POST', 'GET'])
def success():
    if 'id' not in session: # tests if the user bypassed the login 
        return redirect('/')
    return render_template('success.html')

    # tests login information
@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    if not EMAIL_REGEX.match(email):
        flash('Email is not valid')
    
    if not len(password) > 7:
        flash('Password is not valid')
    
    # checks that no flags were raised in the login process
    if not '_flashes' in session:
        try:
            query = 'SELECT * FROM users WHERE email = :email'
            data = {'email' : email}
            user = mysql.query_db(query, data)
            hashed = user[0]['password']
            logged_in = bcrypt.check_password_hash(hashed, password)
        except:
            flash('Invalid email or password')
            logged_in = False

        if logged_in:
            session['id'] = user[0]['id']
            return redirect('/success')
        else:
            flash('Invalid email or password')
    return redirect('/')

app.run(debug=True)