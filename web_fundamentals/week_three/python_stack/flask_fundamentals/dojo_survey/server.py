from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
  return render_template("index.html")
@app.route('/process', methods=['GET', 'POST'])
def process():
   print("Got to the process route")
   name= request.form['name']
   location = request.form['location']
   language = request.form["language"]
   comment = request.form["comment"]
   return render_template('process.html', name = name, location = location, language=language, comment = comment)
   return redirect('/')
app.run(debug=True) # run our server