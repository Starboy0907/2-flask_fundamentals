from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "key_glock"

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

@app.route('/show')
def show():
    return render_template('show.html')  
# Never render a template on a POST request
#Instead we will redirect to our index route
if __name__=="__main__":
    app.run(debug=True)
