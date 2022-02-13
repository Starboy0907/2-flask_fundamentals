from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'frankadank'

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    print('GOT POST INFO')
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['optradio'] = request.form['optradio']
    session['text'] = request.form['text']
    session['remember'] = request.form['remember']
    return redirect('/results')

@app.route('/results')
def results():
    return render_template('results.html')





if __name__=="__main__":
    app.run(debug=True)
