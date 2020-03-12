from flask import Flask, render_template, request, redirect                                         
app = Flask(__name__)                                                             
@app.route('/')                           
def index():
  return render_template('index.html', user_name = "Mary") 
@app.route('/process', methods=['post'])
def process():
  print "Information from the Index Page was received"
  name = request.form['name']
  return redirect('/')
app.run(debug=True)  # Run the app in debug mode.