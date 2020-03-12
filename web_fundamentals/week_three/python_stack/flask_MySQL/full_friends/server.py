from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'fullFriendsdb')
@app.route('/')
def index():
    query = "SELECT * FROM fullFriends"                           
    fullFriends = mysql.query_db(query)                           
    return render_template('index.html', all_friends=fullFriends) 
@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO fullFriends (first_name, last_name, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'occupation': request.form['occupation']
           }
    mysql.query_db(query, data)
    return redirect('/')                            
app.run(debug=True)