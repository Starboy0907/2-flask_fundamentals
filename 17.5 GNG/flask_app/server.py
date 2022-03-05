from flask import Flask, render_template, request, redirect, session
import random
app =Flask(__name__)
app.secret_key = 'hush'
guesses = 0

@app.route('/')
def random_num():
    num = random.randint(1,100)
    guesses = 0
    session['guesses'] = guesses
    session['num'] = num
    print(session['num'])
    return render_template('index.html', num=num, guesses=session['guesses'])

@app.route('/guess', methods=['POST'])
def guess():
    print("Got Post Info")
    print(request.form)
    session['tess'] = request.form['tess']
    return redirect('/result')


@app.route('/result')
def take():
    session['guesses'] += 1
    return render_template('result.html', num=session['num'], tess=int(session['tess']),guesses=session['guesses'])

if __name__ == "__main__":
    app.run(debug=True)
