from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = 'super secret key'


@app.route('/')
def index():
    if not 'die_counter' in session:
        session['die_counter'] = 0
    return render_template('index.html')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

@app.route('/school')
def school():
    session['die_counter'] += 1
    return render_template('school.html')

@app.route('/no_school')
def no_school():
    return render_template('no_school.html')

@app.route('/tv')
def tv():
    session['die_counter'] += 1
    return render_template('tv.html')

@app.route('/no_tv')
def no_tv():
    return render_template('no_tv.html')

@app.route('/live')
def live():
    return render_template('live.html')

@app.route('/die')
def die():
    session['die_counter'] += 1
    return render_template('die.html')

app.run(debug=True)