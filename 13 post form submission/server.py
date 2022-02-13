from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def form():
    return render_template('forms.html')

@app.route('/users', methods=['POST'])
def create_user():
    print('Get Post Info')
    print(request.form)
# Never render a template on a POST request
#Instead we will redirect to our index route
if __name__=="__main__":
    app.run(debug=True)
