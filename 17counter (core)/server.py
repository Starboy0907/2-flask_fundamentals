from flask import Flask, redirect, render_template, session, request
app = Flask(__name__)
app.secret_key = "Keep it DRY"


@app.route('/')
def index():
    if "count" not in session:
        session['count'] = 1
    else:
        session['count'] += 1
    return render_template('index.html')


@app.route('/count', methods=['POST'])
def view_count():
    if request.form['alter']=='add':
        session["count"] += 1
    elif request.form['alter']=="reset":
        session['count'] = 0
    return redirect('/')

@app.route('/increment', methods=['POST'])
def increment():
    num = request.form['inc']
    if request.form['inc']==num:
        session['count'] += int(num) - int(1)
    return redirect('/')


@app.route('/destroy')
def destroy():
    session.clear()
    return redirect('/')



if __name__=="__main__":
    app.run(debug=True)




