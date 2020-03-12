from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
@app.route('/')
def index():
  return render_template("index.html")
@app.route('/process', methods=['GET', 'POST'])
def process():
  print("Got to the process route")
  name = request.form['name']
  if len(request.form['name']) < 1:
    flash("Name cannot be empty!") 
  else:
    flash("Success! Your name is {}".format(request.form['name'])) 
  location = request.form['location']
  language = request.form['language']
  comment= request.form['comment']
  if len(request.form['comment']) > 120:
    flash("comment cannot be longer than 120 characters!") 
  else:
    flash("Success! Your comment has been submitted!") 
  return render_template('process.html', name = name, location = location, language=language, comment = comment)
  return redirect('/')
app.run(debug=True) # run our server