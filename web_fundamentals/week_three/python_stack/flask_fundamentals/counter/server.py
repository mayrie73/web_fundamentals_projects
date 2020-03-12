from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = 'super secret key'


@app.route('/')
def index():
    if not 'page_view' in session:
        session['page_view'] = 1
    return render_template('index.html')
@app.route('/reload')
def reload():
    session['page_view'] += 2
    return redirect('/')
@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')
app.run(debug=True)