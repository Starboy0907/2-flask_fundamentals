from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    session['gold'] = random.randint(5-10)
    print(session['gold'])
    session['total_gold'] = request.form['total_gold']
    session['activities'] = request.form['activities']
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
