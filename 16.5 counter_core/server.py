from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "shhh"

@app.route('/')
def index():
    if "count" not in session:
        session['count'] = 1
    else:
        session['count'] += 1
    return render_template('index.html')

@app.route('/increment', methods=["POST"])
def inc():
    num = request.form['inc']
    if request.form['inc']== num:
        session['count'] += int(num)
    return redirect('/')    
    

@app.route('/count', methods=['POST'])
def view_count():
    if request.form['alter']=='add':
        session["count"] += 1
    elif request.form['alter']=='reset':
        session['count'] = 0
    elif request.form['alter']=='destroy':
        session.clear()
    return redirect('/')

@app.route('/count2', methods=['POST'])
def count_2():
    num = request.form['inc']
    if request.form['inc']==num:
        session['count'] += int(num) - int(1)
    return redirect('/')    

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
    