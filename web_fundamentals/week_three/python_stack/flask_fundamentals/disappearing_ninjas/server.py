from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
  return render_template('index.html') 
@app.route('/ninja')
def ninja():
  return render_template('ninja.html')
@app.route('/ninja_blue')
def ninja_blue():
  return render_template('ninja_blue.html')
@app.route('/ninja_orange')
def ninja_orange():
  return render_template('ninja_orange.html')
@app.route('/ninja_purple')
def ninja_purple():
  return render_template('ninja_purple.html')
@app.route('/ninja_red')
def ninja_red():
  return render_template('ninja_red.html')
@app.route('/ninja_black')
def ninja_black():
  return render_template('ninja_black.html')
@app.route('/ninja_123')
def ninja_123():
  return render_template('ninja_123.html')
app.run(debug=True) # run our server

