from flask import Flask, render_template, request,redirect,session
app = Flask(__name__)
app.secret_key = "cash"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    print("GOT POST INFO")
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['favorite_lang'] = request.form['favorite_lang']
    return redirect('/results')

@app.route('/results')
def results():
    return render_template('results.html')

if __name__ =="__main__":
    app.run(debug=True)
