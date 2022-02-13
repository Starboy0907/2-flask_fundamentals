from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def table():
    users = [

        {'first_name' : 'Micheal', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name': 'Mark', 'last_name' : 'Guillen'},
        {'first_name': 'KB', 'last_name' :'Tone'}
    ]
    print(request.form)
    return render_template('index.html', users = users) 


if __name__=="__main__":
    app.run(debug=True)




