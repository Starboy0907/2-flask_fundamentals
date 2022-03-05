from flask import Flask, render_template,redirect, request, session
app = Flask(__name__)
app_key = "Snufalufagas"

@app.route('/')
def form():
    return render_template('forms.html')

@app.route('/process', methods=["POST"])
def form_test():
    print("Got Post Info")
    print(request.form)
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']
    return redirect('/show')

    #adding this method
# @app.route("/show")
# def show_user():
#     return render_template('show.html', fname_on_template=session['first_name'],lname_on_template=session['last_name'], email_on_template=session['email'])

@app.route('/show')
def show_user():
    return render_template('show.html')

if __name__ == "__main__":
    app.run(debug=True)
